# Altair

A Reflex custom component for altair charts.

## Installation

```bash
pip install reflex-altair
```

# Altair Component

The `Altair` component is a React component that integrates with the `react-vega` library to render Vega 
and Vega-Lite visualizations in your application. This component allows you to specify the chart specifications,
 data, and various configuration options to customize the rendering and behavior of the visualizations.

> It supports [altair python library](https://altair-viz.github.io/index.html) !

## Props

### `spec`

- **Type:** `AltairChart | Dict[str, Any]`
- **Description:** The Vega or Vega-Lite chart specification. This can be an instance of [AltairChart](/altair/custom_components/reflex_altair/type.py#L4) or a dictionary representing the chart specification.

### `data`

- **Type:** `Dict[str, List[Dict[str, Any]]]`
- **Description:** The data to be used in the chart. This should be a dictionary where the keys are dataset names and the values are lists of observations.

> Transform your dataframe like this
```python
df.to_dict("records")
```
### `on_error`

- **Type:** `rx.EventHandler[lambda _e: [_e]]`
- **Description:** Event handler that is triggered when an error occurs during the rendering of the chart.


### `mode`

- **Type:** `"vega" | "vega-lite"`
- **Description:** The mode in which the chart should be rendered. This can be used to specify whether the chart should be rendered in `vega` or `vega-lite` mode.

### `actions`

- **Type:** `bool | AltairAction`
- **Description:** Configuration for the action menu that appears in the top-right corner of the chart. This can be a boolean to enable/disable the menu or an [AltairAction](/altair/custom_components/reflex_altair/type.py#L64) object to customize the actions.

### `download_file_name`

- **Type:** `str`
- **Description:** The default file name to use when downloading the chart as an image.

### `log_level`

- **Type:** `0 - 5`
- **Description:** The log level for the Vega parser. This can be used to control the verbosity of the logging output.

### `renderer`

- **Type:** `AltairRenderer`
- **Description:** The renderer to use for the chart. This can be set to `canvas` or `svg`.

### `tooltip`

- **Type:** `bool`
- **Description:** Boolean flag to enable or disable tooltips in the chart.
> False overwrite tooltips from spec 

### `padding`

- **Type:** `Union[int, float] | Dict[AltairPadding, Union[int, float]]]`
- **Description:** Padding around the chart. This can be a single value applied 
to all sides or a dictionary specifying different padding values for each side.
Values are `left`, `right`, `bottom`, `left`
> used instead of default style padding

### Events
`on_new_view` depends on :
- on_new_view_click
- on_new_view_dblclick
- on_new_view_dragenter
- on_new_view_dragleave
- on_new_view_dragover
- on_new_view_keydown
- on_new_view_keypress
- on_new_view_keyup
- on_new_view_mousedown
- on_new_view_mousemove
- on_new_view_mouseout
- on_new_view_mouseover
- on_new_view_mouseup
- on_new_view_mousewheel
- on_new_view_touchend
- on_new_view_touchmove
- on_new_view_touchstart
- on_new_view_wheel

> Chart is rerender after an event, removing current selection

`signal_listeners`is not yet supported

## Example Usage
With [altair](https://altair-viz.github.io/index.html)

```python
import altair as alt
import pandas as pd

# Define the data
chart_data = {
    "dataset_id": pd.DataFrame(
        {
            "category": ["A", "B", "C"],
            "value": [28, 55, 43]
        }
    ).to_dict("records")
}

# Define the chart
chart_spec = alt.Chart(alt.Data(name="dataset_id")).mark_bar().encode(
    x='category:O',
    y='value:Q',
    tooltip=['category', 'value']
).properties(
    title='Bar Chart Example'
)
```
With [vega-lite](https://vega.github.io/vega-lite/)
```python
chart_spec = {
    "data": {"name": "table"},
    "mark": "bar",
    "encoding": {
        "x": {"field": "category", "type": "nominal"},
        "y": {"field": "value", "type": "quantitative"}
    }
}

chart_data = {
    "table": [
        {"category": "A", "value": 28},
        {"category": "B", "value": 55},
        {"category": "C", "value": 43}
    ]
}
```
```python
# Create the altair component
altair_component = altair_chart(
    spec=chart_spec,
    data=chart_data,
    actions={"export": {"svg": False}, "compiled": False},
    download_file_name="filename",
)
```

You can run [reflex demo](./altair_demo) also