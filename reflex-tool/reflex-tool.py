"""Main application file."""
import reflex as rx
from .state import State
from .pages import (
    home_page,
    quantization_page,
    inference_page,
    performance_page,
    contact_page,
)


# Create app and add pages
app = rx.App()
app.add_page(home_page, route="/")
app.add_page(quantization_page, route="/quantization")
app.add_page(inference_page, route="/inference")
app.add_page(performance_page, route="/performance")
app.add_page(contact_page, route="/contact")
