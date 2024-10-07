# Altair - Vega

A Reflex custom component for Vega grammar that support altair charts.

## Installation

```bash
pip install TODO
```

# Vega Component

The `Vega` component is a React component that integrates with the `react-vega` library to render Vega 
and Vega-Lite visualizations in your application. This component allows you to specify the chart specifications,
 data, and various configuration options to customize the rendering and behavior of the visualizations.

> It supports [altair python library](https://altair-viz.github.io/index.html) !

## Props

### `spec`

- **Type:** `AltairChart | Dict[str, Any]`
- **Description:** The Vega or Vega-Lite chart specification. This can be an instance of [AltairChart](/vega/custom_components/reflex_vega/type.py#L4) or a dictionary representing the chart specification.

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
- **Description:** Configuration for the action menu that appears in the top-right corner of the chart. This can be a boolean to enable/disable the menu or an [AltairAction](/vega/custom_components/reflex_vega/type.py#L64) object to customize the actions.

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
`signal_listeners` and `on_new_view` are not yet supported

## Example Usage
With [vega](https://vega.github.io/vega/)


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

```python
# Create the Vega component
vega_chart = vega(
    spec=chart_spec,
    data=chart_data,
    actions={"export": {"svg": False}, "compiled": False},
    download_file_name="filename",
)
```

You can run [reflex demo](vega/vega_demo) also