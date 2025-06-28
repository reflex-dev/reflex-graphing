import io
import base64
from matplotlib.figure import Figure
import matplotlib
from reflex.components.component import Component
from reflex.components.next.image import Image
from reflex.utils.serializers import serializer


matplotlib.use("Agg")


class Pyplot(Component):
    """Display a Matplotlib chart."""

    @classmethod
    def create(cls, fig: Figure, **props):
        """Create a Pyplot component."""
        return Image.create(src=fig, **props)

    @staticmethod
    @serializer
    def serialize_matplotlib_figure(fig: Figure) -> str:
        """Serialize the Matplotlib figure to a base64-encoded PNG image."""
        buf = io.BytesIO()
        fig.savefig(buf, format="png", bbox_inches="tight")
        buf.seek(0)
        img_base64 = base64.b64encode(buf.getvalue()).decode("utf-8")
        return f"data:image/png;base64,{img_base64}"


pyplot = Pyplot.create
