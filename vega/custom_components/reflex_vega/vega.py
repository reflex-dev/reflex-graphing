from typing import Dict, Any, List, Union, Literal
from .type import AltairSignal, AltairChart, AltairAutosize, AltairBounds, AltairLogLevel
import reflex as rx


class Vega(rx.Component):
    library = "react-vega"
    tag = "Vega"

    spec: rx.Var[AltairChart | Dict[str, Any]]
    data: rx.Var[Dict[str, List[Dict[str, Any]]]]

    padding: rx.Var[Union[int, float]]
    background: rx.Var[str]  # TODO type ?

    description: rx.Var[str]
    autosize: rx.Var[AltairAutosize]

    center: rx.Var[bool]
    bounds: rx.Var[AltairBounds]

    spacing: rx.Var[Union[int, float]]

    log_level: rx.Var[AltairLogLevel]

    # signal_listeners: rx.Var[Dict[AltairSignal, rx.EventHandler[lambda _e: [_e]]]]
    # on_new_view: rx.Var[Dict[AltairSignal, rx.EventHandler[lambda _e: [_e]]

    # TODO implement create methode to construct on_new_view and signal_listeners
    # on_new_view and signal_listeners should depend of following child event attributes
    #
    # on_click
    # on_dblclick
    # on_dragenter
    # on_dragleave
    # on_dragover
    # on_keydown
    # on_keypress
    # on_keyup
    # on_mousedown
    # on_mousemove
    # on_mouseout
    # on_mouseover
    # on_mouseup
    # on_mousewheel
    # on_touchend
    # on_touchmove
    # on_touchstart
    # on_wheel
    #
    # """
    # onNewView={
    #   (view) => {
    #     view.addEventListener("click", (_e, item) => console.log(item));
    #     view.addEventListener("dblclick", (_e, item) => console.log(item));
    #     view.addEventListener("dragenter", (_e, item) => console.log(item));
    #     view.addEventListener("dragleave", (_e, item) => console.log(item));
    #     view.addEventListener("dragover", (_e, item) => console.log(item));
    #     view.addEventListener("keydown", (_e, item) => console.log(item));
    #     view.addEventListener("keypress", (_e, item) => console.log(item));
    #     view.addEventListener("keyup", (_e, item) => console.log(item));
    #     view.addEventListener("mousedown", (_e, item) => console.log(item));
    #     view.addEventListener("mousemove", (_e, item) => console.log(item));
    #     view.addEventListener("mouseout", (_e, item) => console.log(item));
    #     view.addEventListener("mouseover", (_e, item) => console.log(item));
    #     view.addEventListener("mouseup", (_e, item) => console.log(item));
    #     view.addEventListener("mousewheel", (_e, item) => console.log(item));
    #     view.addEventListener("touchend", (_e, item) => console.log(item));
    #     view.addEventListener("touchmove", (_e, item) => console.log(item));
    #     view.addEventListener("touchstart", (_e, item) => console.log(item));
    #     view.addEventListener("wheel", (_e, item) => console.log(item));
    #   }
    # }
    # """
    #


vega = Vega.create
