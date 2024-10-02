import reflex as rx
import numpy as np
import matplotlib.pyplot as plt
from .pyplot import reflex_pyplot
from reflex.style import toggle_color_mode

def create_plot(theme: str):
    """Create a plot with the same data for both dark and light themes.
    
    Args:
        theme: The theme to create ('dark' or 'light').
    
    Returns:
        The plot figure.
    """
    bg_color = '#1e1e1e' if theme == 'dark' else 'white'
    text_color = 'white' if theme == 'dark' else 'black'
    grid_color = '#555555' if theme == 'dark' else '#cccccc'
    
    fig, ax = plt.subplots(facecolor=bg_color)
    ax.set_facecolor(bg_color)
    
    # Generate data once
    n = 100
    colors = ["#4e79a7", "#f28e2b", "#59a14f"]
    for color in colors:
        x, y = np.random.rand(2, n)
        scale = 100.0 * np.random.rand(n)
        ax.scatter(x, y, c=color, s=scale, label=color, alpha=0.6, edgecolors="none")
    
    ax.legend(facecolor=bg_color, edgecolor='none', labelcolor=text_color)
    ax.grid(True, color=grid_color)
    ax.tick_params(colors=text_color)
    ax.xaxis.label.set_color(text_color)
    ax.yaxis.label.set_color(text_color)
    ax.title.set_color(text_color)
    return fig

class State(rx.State):
    plot_data: tuple = (np.random.rand(2, 100), np.random.rand(2, 100), np.random.rand(2, 100))
    
    def randomize(self):
        self.plot_data = (np.random.rand(2, 100), np.random.rand(2, 100), np.random.rand(2, 100))
    
    @rx.cached_var
    def fig_light(self) -> plt.Figure:
        return self.create_themed_plot('light')
    
    @rx.cached_var
    def fig_dark(self) -> plt.Figure:
        return self.create_themed_plot('dark')
    
    def create_themed_plot(self, theme: str) -> plt.Figure:
        fig = create_plot(theme)
        ax = fig.gca()
        colors = ["#4e79a7", "#f28e2b", "#59a14f"]
        for i, color in enumerate(colors):
            x, y = self.plot_data[i]
            scale = 100.0 * np.random.rand(100)
            ax.scatter(x, y, c=color, s=scale, label=color, alpha=0.6, edgecolors="none")
        return fig

def index():
    return rx.center(
        rx.card(
            rx.color_mode_cond(
                reflex_pyplot(State.fig_light, width="100%", height="height"),
                reflex_pyplot(State.fig_dark, width="100%", height="height"),
            ),
            rx.button("Randomize", on_click=State.randomize),
            rx.button(
                "Toggle Color Mode",
                on_click=toggle_color_mode,
                margin_left="1rem",
            ),
            width="100%",
            height="100%",
        )
    )



app = rx.App()
app.add_page(index) 
