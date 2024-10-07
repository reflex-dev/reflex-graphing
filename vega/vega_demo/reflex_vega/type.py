from typing import Union, Literal, Optional, Dict
import altair as alt

AltairChart = Union[
    alt.Chart,
    alt.VConcatChart,
    alt.HConcatChart,
    alt.FacetChart,
    alt.LayerChart,
    alt.ConcatChart,
    alt.RepeatChart,
]

AltairSignal = Literal[
    "click",
    "dblclick",
    "dragenter",
    "dragleave",
    "dragover",
    "keydown",
    "keypress",
    "keyup",
    "mousedown",
    "mousemove",
    "mouseout",
    "mouseover",
    "mouseup",
    "mousewheel",
    "touchend",
    "touchmove",
    "touchstart",
    "wheel",
]

AltairLogLevel = Literal[
    0,
    1,
    2,
    3,
    4,
    5
]

AltairPadding = Literal[
    "left",
    "right",
    "top",
    "bottom",
]
# AltairDataFrame = NewType('AltairDataFrame', pd.DataFrame)

AltairMode = Literal[
    "vega",
    "vega-lite"
]

AltairRenderer = Literal[
    'canvas',
    'svg',
    'hybrid',
    'none'
]

AltairAction = Union[
    bool,
    Dict[Literal['export', 'source', 'compiled', 'editor'], bool],
    Dict[Literal['export'], Dict[Literal['svg', 'png'], Optional[bool]]]
]
