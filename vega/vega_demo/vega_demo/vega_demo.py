"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from typing import Dict, List, Any

import reflex as rx

from reflex_vega.type import AltairChart
from rxconfig import config
from reflex_vega.vega import vega
from vega_demo.altair.country_pop import DATA, SPEC
from vega_demo.altair.seattle_weather import seattle_weather_dashboard
from vega_datasets import data


class State(rx.State):
    """The app state."""

    # TODO custom serializer for pandas dataframe records
    data_1: Dict[str, List[Dict[str, Any]]] = {"seattle_weather": data.seattle_weather().to_dict("records")}
    spec_1: AltairChart = seattle_weather_dashboard()

    data_2: Dict[str, List[Dict[str, Any]]] = DATA
    spec_2: Dict[str, Any] = SPEC


def index() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            vega(
                spec=State.spec_1,
                data=State.data_1,
                log_level=0
            ),
            vega(
                spec=State.spec_2,
                data=State.data_2,
                padding=10,
                log_level=5
            ),
        ),
    )


app = rx.App()
app.add_page(index)
