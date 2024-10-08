import reflex as rx
import numpy as np
import matplotlib.pyplot as plt
from custom_components.reflex_pyplot import pyplot
from reflex.style import toggle_color_mode
import random

def create_plot(theme: str, plot_data: tuple, scale: list):
    bg_color, text_color = ('#1e1e1e', 'white') if theme == 'dark' else ('white', 'black')
    grid_color = '#555555' if theme == 'dark' else '#cccccc'
    
    fig, ax = plt.subplots(facecolor=bg_color)
    ax.set_facecolor(bg_color)
    
    for (x, y), color in zip(plot_data, ["#4e79a7", "#f28e2b", "#59a14f"]):
        ax.scatter(x, y, c=color, s=scale, label=color, alpha=0.6, edgecolors="none")
    
    ax.legend(facecolor=bg_color, edgecolor='none', labelcolor=text_color)
    ax.grid(True, color=grid_color)
    ax.tick_params(colors=text_color)
    for spine in ax.spines.values():
        spine.set_edgecolor(text_color)
    
    for item in [ax.xaxis.label, ax.yaxis.label, ax.title]:
        item.set_color(text_color)
    
    return fig

class State(rx.State):
    num_points: int = 100
    plot_data: tuple = tuple(np.random.rand(2, 100) for _ in range(3))
    scale: list = [random.uniform(0, 100) for _ in range(100)]
    
    def randomize(self):
        self.plot_data = tuple(np.random.rand(2, self.num_points) for _ in range(3))
        self.scale = [random.uniform(0, 100) for _ in range(self.num_points)]
    
    def set_num_points(self, num_points: list[int]):
        self.num_points = num_points[0]
        print(self.num_points)
        self.randomize()
    
    @rx.var
    def fig_light(self) -> plt.Figure:
        fig = create_plot('light', self.plot_data, self.scale)
        plt.close(fig)  # Close the figure after creating it
        return fig
    
    @rx.var
    def fig_dark(self) -> plt.Figure:
        fig = create_plot('dark', self.plot_data, self.scale)
        plt.close(fig)  # Close the figure after creating it
        return fig

def index():
    return rx.vstack(
        rx.card(
            rx.color_mode_cond(
                pyplot(State.fig_light, width="100%", height="height"),
                pyplot(State.fig_dark, width="100%", height="height"),
            ),
            rx.vstack(
                rx.hstack(  
                    rx.button("Randomize", on_click=State.randomize),
                    rx.button("Toggle Color Mode", on_click=toggle_color_mode),
                ),
                rx.text("Number of Points:"),
                rx.slider(
                    default_value=100,
                    min_=10,
                    max=1000,
                    on_value_commit=State.set_num_points,
                ),
                width="100%",
            ),
            width="50%",
        ),
        justify_content="center",
        align_items="center",
        height="100vh",
    )

app = rx.App()
app.add_page(index)
