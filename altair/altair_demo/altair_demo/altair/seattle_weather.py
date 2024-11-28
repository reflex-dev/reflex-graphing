import altair as alt

from reflex_altair.type import AltairChartType


def seattle_weather_dashboard() -> AltairChartType:
    """
    Source: https://altair-viz.github.io/gallery/seattle_weather_interactive.html
    """

    scale = alt.Scale(domain=['sun', 'fog', 'drizzle', 'rain', 'snow'],
                      range=['#e7ba52', '#a7a7a7', '#aec7e8', '#1f77b4', '#9467bd'])
    color = alt.Color('weather:N', scale=scale)

    brush = alt.selection_interval(encodings=['x'])
    click = alt.selection_point(encodings=['color'])  # on='touchstart' for mobile

    points = alt.Chart().mark_point().encode(
        alt.X('monthdate(date):T', title='Date'),
        alt.Y('temp_max:Q',
              title='Maximum Daily Temperature (C)',
              scale=alt.Scale(domain=[-5, 40])
              ),
        tooltip=alt.Tooltip(["weather:N", "temp_max:Q"]),
        color=alt.condition(brush, color, alt.value('lightgray')),
        size=alt.Size('precipitation:Q', scale=alt.Scale(range=[5, 200]))
    ).properties(
        width="container",
        height=300
    ).add_params(
        brush
    ).transform_filter(
        click
    )

    # Bottom panel is a bar chart of weather type
    bars = alt.Chart().mark_bar().encode(
        x='count()',
        y='weather:N',
        color=alt.condition(click, color, alt.value('lightgray')),
    ).transform_filter(
        brush
    ).properties(
        width="container",
    ).add_params(
        click,
    )

    return alt.vconcat(
        points,
        bars,
        data=alt.Data(name="seattle_weather"),
        title="Seattle Weather: 2012-2015",

    )
