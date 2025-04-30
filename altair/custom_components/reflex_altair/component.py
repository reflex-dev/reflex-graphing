from typing import Dict, Any, List, Union

from .type import AltairChartType, AltairLogLevel, AltairPadding, \
    AltairMode, \
    AltairRenderer, AltairAction, AltairSignal
import reflex as rx


SIGNAL_PROPS = {"onNewView" + e.title(): e for e in AltairSignal.__args__}


class AltairChart(rx.NoSSRComponent):
    library = "react-vega"
    tag = "Vega"
    alias = "Altair"

    spec: rx.Var[AltairChartType | Dict[str, Any]]
    data: rx.Var[Dict[str, List[Dict[str, Any]]]]

    # signal_listeners: rx.Var[Dict[AltairSignal, rx.EventHandler[lambda _e: [_e]]]]
    on_new_view: Any = {}

    on_new_view_click: rx.EventHandler[lambda _e: [_e]]
    on_new_view_dblclick: rx.EventHandler[lambda _e: [_e]]
    on_new_view_dragenter: rx.EventHandler[lambda _e: [_e]]
    on_new_view_dragleave: rx.EventHandler[lambda _e: [_e]]
    on_new_view_dragover: rx.EventHandler[lambda _e: [_e]]
    on_new_view_keydown: rx.EventHandler[lambda _e: [_e]]
    on_new_view_keypress: rx.EventHandler[lambda _e: [_e]]
    on_new_view_keyup: rx.EventHandler[lambda _e: [_e]]
    on_new_view_mousedown: rx.EventHandler[lambda _e: [_e]]
    on_new_view_mousemove: rx.EventHandler[lambda _e: [_e]]
    on_new_view_mouseout: rx.EventHandler[lambda _e: [_e]]
    on_new_view_mouseover: rx.EventHandler[lambda _e: [_e]]
    on_new_view_mouseup: rx.EventHandler[lambda _e: [_e]]
    on_new_view_mousewheel: rx.EventHandler[lambda _e: [_e]]
    on_new_view_touchend: rx.EventHandler[lambda _e: [_e]]
    on_new_view_touchmove: rx.EventHandler[lambda _e: [_e]]
    on_new_view_touchstart: rx.EventHandler[lambda _e: [_e]]
    on_new_view_wheel: rx.EventHandler[lambda _e: [_e]]

    on_error: rx.EventHandler[lambda _e: [_e]]

    mode: rx.Var[AltairMode]

    actions: rx.Var[AltairAction]
    download_file_name: rx.Var[str]

    log_level: rx.Var[AltairLogLevel]

    renderer: rx.Var[AltairRenderer]

    tooltip: rx.Var[bool]

    padding: rx.Var[Union[int, float] | Dict[AltairPadding, Union[int, float]]]

    def add_hooks(self) -> list[str | rx.Var[str]]:
        tag = self._render()

        def js_code(event, placeholder):
            props_event = "on_new_view_" + event
            if isinstance(self.event_triggers[props_event], rx.Var):
                placeholder = str(self.event_triggers[props_event])
            else:
                placeholder = placeholder.upper()
            return f"""
        view.addEventListener("{event}", (_e, item) => {{
            if (item === null)
                    return null
            const {{ items, context, datum, ...item2 }} = item
            const {{ mark, ...datum2 }} = datum
            {placeholder}(
                [_e.vegaType, datum2]
            )
        }}, false);
        """

        listeners = "\n".join([
            js_code(SIGNAL_PROPS[key], key)
            for key in SIGNAL_PROPS & tag.props.keys()
        ])

        if listeners:
            self.on_new_view = rx.Var(_js_expr=
                     f"""
                    (view) => {{
                        {listeners}
                    }}
                    """
                )

        return []


altair_chart = AltairChart.create
