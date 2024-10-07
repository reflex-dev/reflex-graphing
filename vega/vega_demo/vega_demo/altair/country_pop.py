SPEC = {
  "$schema": "https://vega.github.io/schema/vega/v5.json",
  "width": 400,
  "height": 200,
  "padding": 5,

  "data": [
    {
      "name": "table",
    }
  ],

  "scales": [
    {
      "name": "xscale",
      "type": "band",
      "domain": {"data": "table", "field": "country"},
      "range": "width",
      #"padding": 0.05
    },
    {
      "name": "yscale",
      "type": "linear",
      "domain": {"data": "table", "field": "population"},
      "range": "height",
      "nice": True
    }
  ],

  "axes": [
    {"orient": "bottom", "scale": "xscale"},
    {"orient": "left", "scale": "yscale"}
  ],

  "marks": [
    {
      "type": "rect",
      "from": {"data": "table"},
      "encode": {
        "enter": {
          "x": {"scale": "xscale", "field": "country"},
          "width": {"scale": "xscale", "band": 1},
          "y": {"scale": "yscale", "field": "population"},
          "y2": {"scale": "yscale", "value": 0}
        },
        "update": {
          "fill": {"value": "steelblue"}
        },
        "hover": {
          "fill": {"value": "red"}
        }
      }
    }
  ]
}


DATA = {
        "table": [
            {"country": "USA", "population": 331002651},
            {"country": "India", "population": 1380004385},
            {"country": "China", "population": 1439323776},
            {"country": "Brazil", "population": 212559417},
            {"country": "Pakistan", "population": 220892340}
        ]
    }