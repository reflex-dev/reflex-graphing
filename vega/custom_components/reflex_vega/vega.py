from typing import Dict, Any, List, Union
from .type import AltairChart, AltairLogLevel, AltairPadding, \
    AltairMode, \
    AltairRenderer, AltairAction
import reflex as rx


class Vega(rx.Component):
    library = "react-vega"
    tag = "Vega"

    spec: rx.Var[AltairChart | Dict[str, Any]]
    data: rx.Var[Dict[str, List[Dict[str, Any]]]]

    # Can't support event for signal_listeners & on_new_view
    # signal_listeners: rx.Var[Dict[AltairSignal, rx.EventHandler[lambda _e: [_e]]]]
    # on_new_view: rx.Var[Dict[AltairSignal, rx.EventHandler[lambda _e: [_e]]]]

    on_error: rx.EventHandler[lambda _e: [_e]]

    mode: rx.Var[AltairMode]

    actions: rx.Var[AltairAction]
    download_file_name: rx.Var[str]

    log_level: rx.Var[AltairLogLevel]

    renderer: rx.Var[AltairRenderer]

    tooltip: rx.Var[bool]

    padding: rx.Var[Union[int, float] | Dict[AltairPadding, Union[int, float]]]


vega = Vega.create
