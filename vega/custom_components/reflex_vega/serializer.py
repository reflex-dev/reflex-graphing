from typing import Dict, Any, List

import reflex as rx
import pandas as pd

from .type import AltairChart


@rx.serializer
def serialize_altair_chart(chart: AltairChart) -> Dict[str, Dict[str, Any]]:
    """
    Serialize an altair Chart to get his Vega spec
    """
    return chart.to_dict()

# TODO allow serializer overwrite in reflex.utils.serializers.serializer
# @rx.serializer
# def serialize_dataframe(dataframe: pd.DataFrame) -> List[Dict[str, Any]]:
#     """
#     Serialize a pandas DataFrame to dict with records
#     """
#     return dataframe.to_dict("records")
