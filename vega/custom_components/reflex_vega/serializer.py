import reflex as rx
from typing import Dict, Any
from reflex_vega.type import AltairChart


@rx.serializer
def serialize_altair_chart(chart: AltairChart) -> Dict[str, Dict[str, Any]]:
    """
    Serialize an altair Chart to get his Vega spec
    """
    return chart.to_dict()

# allow serializer overwrite in reflex.utils.serializers.serializer
# @rx.serializer
# def serialize_altair_dataframe(dataframe: AltairDataFrame) -> List[Dict[str, Any]]:
#     """
#     Serialize a pandas DataFrame to dict with records
#     """
#     return dataframe.to_dict("records")
