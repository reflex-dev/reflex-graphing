SPEC = {
    "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
    "description": "An interactive visualization of connections among major U.S. "
    "airports in 2008. Based on a U.S. airports example by Mike "
    "Bostock.",
    "height": 500,
    "layer": [
        {
            "data": {
                "format": {"feature": "states", "type": "topojson"},
                "url": "data/us-10m.json",
            },
            "mark": {
                "fill": "#ddd",
                "stroke": "#fff",
                "strokeWidth": 1,
                "type": "geoshape",
            },
        },
        {
            "data": {"url": "data/flights-airport.csv"},
            "encoding": {
                "latitude": {"field": "latitude"},
                "latitude2": {"field": "lat2"},
                "longitude": {"field": "longitude"},
                "longitude2": {"field": "lon2"},
            },
            "mark": {"color": "#000", "opacity": 0.35, "type": "rule"},
            "transform": [
                {"filter": {"empty": False, "param": "org"}},
                {
                    "from": {
                        "data": {"url": "data/airports.csv"},
                        "fields": ["latitude", "longitude"],
                        "key": "iata",
                    },
                    "lookup": "origin",
                },
                {
                    "as": ["lat2", "lon2"],
                    "from": {
                        "data": {"url": "data/airports.csv"},
                        "fields": ["latitude", "longitude"],
                        "key": "iata",
                    },
                    "lookup": "destination",
                },
            ],
        },
        {
            "data": {"url": "data/flights-airport.csv"},
            "encoding": {
                "latitude": {"field": "latitude"},
                "longitude": {"field": "longitude"},
                "order": {"field": "routes", "sort": "descending"},
                "size": {
                    "field": "routes",
                    "legend": None,
                    "scale": {"rangeMax": 1000},
                    "type": "quantitative",
                },
            },
            "mark": {"type": "circle"},
            "params": [
                {
                    "name": "org",
                    "select": {
                        "fields": ["origin"],
                        "nearest": True,
                        "on": "pointerover",
                        "type": "point",
                    },
                }
            ],
            "transform": [
                {"aggregate": [{"as": "routes", "op": "count"}], "groupby": ["origin"]},
                {
                    "from": {
                        "data": {"url": "data/airports.csv"},
                        "fields": ["state", "latitude", "longitude"],
                        "key": "iata",
                    },
                    "lookup": "origin",
                },
                {"filter": "datum.state !== 'PR' && datum.state !== 'VI'"},
            ],
        },
    ],
    "projection": {"type": "albersUsa"},
    "width": 900,
}
