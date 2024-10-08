import json
from typing import Dict, List, Any
import logging
import reflex as rx

from reflex_altair.type import AltairChartType
from reflex_altair.component import altair_chart
from reflex_monaco import monaco
from altair_demo.altair.country_pop import DATA, SPEC
from altair_demo.altair.seattle_weather import seattle_weather_dashboard
from vega_datasets import data
import altair as alt


class State(rx.State):
    """The app state."""
    data_1: Dict[str, List[Dict[str, Any]]] = {"seattle_weather": data.seattle_weather().to_dict("records")}
    spec_1: AltairChartType = seattle_weather_dashboard()
    theme: str = "default"

    data_2: Dict[str, List[Dict[str, Any]]] = DATA
    spec_2: Dict[str, Any] = SPEC

    def set_theme(self, value):
        self.theme = value
        alt.themes.enable(self.theme)
        self.spec_1 = seattle_weather_dashboard()

    def monaco_edit(self, value):
        try:
            tmp = json.loads(value)
            self.spec_2 = tmp
        except Exception as e:
            logging.error(e)

    @rx.vars.base.computed_var()
    def json_spec_2(self) -> str:
        return json.dumps(self.spec_2, indent=2)


def theme_dropdown() -> rx.Component:
    return rx.select.root(
        rx.select.trigger(),
        rx.select.content(
            rx.select.group(
                rx.foreach(
                    list(alt.themes._plugins),
                    lambda x: rx.select.item(
                        x, value=x
                    ),
                )
            ),
        ),
        value=State.theme,
        default_value=State.theme,
        on_change=State.set_theme,
    )


def index() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("From altair python"),
            theme_dropdown(),
            altair_chart(
                spec=State.spec_1,
                data=State.data_1,
                width="100%",
                actions={"export": {"svg": False}, "compiled": False},
            ),
            rx.markdown("""
            ### Backend :
            It is recommended to use `alt.Data` to pass data as props
            ```python
            alt.Chart(
                data=alt.Data(name="seattle_weather")
                ...
            ).properties(
                width="container", # add "container" instead of a numeric value to make your chart responsive
            )
            ```
            ### Frontend :
            ```js
            vega(
                spec=State.spec_1,
                data=State.data_1,
            )
            ```
            """),
            rx.heading("From vega-lite JSON"),
            altair_chart(
                spec=State.spec_2,
                data=State.data_2,
            ),
            monaco(
                default_value=State.json_spec_2,
                on_change=State.monaco_edit,
                width="600px",
                height="200px"
            ),
        ),
    )


app = rx.App()
app.add_page(index)
