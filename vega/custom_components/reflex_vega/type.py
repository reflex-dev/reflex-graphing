from typing import Union, Literal
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

AltairAutosize = Literal[
    "pad",
    "fit",
    "fit-x",
    "fit-y",
    "none"
]

AltairBounds = Literal[
    "flush",
    "full"
]


AltairLogLevel = Literal[
    0,
    1,
    2,
    3,
    4,
    5
]
