"""Main application file."""
import reflex as rx
from .pages import (
    quantization_page,
    inference_page,
    performance_page,
    contact_page,
)


class State(rx.State):
    """Application state."""
    pass


# Create app and add pages
app = rx.App()
app.add_page(quantization_page, route="/")
app.add_page(inference_page, route="/inference")
app.add_page(performance_page, route="/performance")
app.add_page(contact_page, route="/contact")
