import reflex as rx
from typing import Dict, Any
from .type import AltairChartType


@rx.serializer
def serialize_altair_chart(chart: AltairChartType) -> Dict[str, Dict[str, Any]]:
    """
    Serialize an altair Chart to get his vega-lite spec
    """
    return chart.to_dict()


# allow serializer overwrite in reflex.utils.serializers.serializer
# @rx.serializer
# def serialize_altair_dataframe(dataframe: AltairDataFrame) -> List[Dict[str, Any]]:
#     """
#     Serialize a pandas DataFrame to dict with records
#     """
#     return dataframe.to_dict("records")
