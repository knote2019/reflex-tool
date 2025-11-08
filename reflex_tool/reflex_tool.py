"""Main application file."""
import reflex as rx
from .pages import (
    home_page,
    quantization_page,
    quantization_ampere_page,
    quantization_ada_page,
    quantization_hopper_page,
    quantization_blackwell_page,
    inference_page,
    inference_ampere_page,
    inference_ada_page,
    inference_hopper_page,
    inference_blackwell_page,
    performance_page,
    performance_ampere_page,
    performance_ada_page,
    performance_hopper_page,
    performance_blackwell_page,
    contact_page,
)


# Create app and add pages
app = rx.App()
app.add_page(home_page, route="/")
app.add_page(quantization_page, route="/quantization")
app.add_page(quantization_ampere_page, route="/quantization/ampere")
app.add_page(quantization_ada_page, route="/quantization/ada")
app.add_page(quantization_hopper_page, route="/quantization/hopper")
app.add_page(quantization_blackwell_page, route="/quantization/blackwell")
app.add_page(inference_page, route="/inference")
app.add_page(inference_ampere_page, route="/inference/ampere")
app.add_page(inference_ada_page, route="/inference/ada")
app.add_page(inference_hopper_page, route="/inference/hopper")
app.add_page(inference_blackwell_page, route="/inference/blackwell")
app.add_page(performance_page, route="/performance")
app.add_page(performance_ampere_page, route="/performance/ampere")
app.add_page(performance_ada_page, route="/performance/ada")
app.add_page(performance_hopper_page, route="/performance/hopper")
app.add_page(performance_blackwell_page, route="/performance/blackwell")
app.add_page(contact_page, route="/contact")
