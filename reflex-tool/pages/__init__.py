"""Pages module."""
from .home import home_page
from .quantization import quantization_page
from .inference import inference_page
from .performance import performance_page
from .contact import contact_page
from .quantization_ampere import quantization_ampere_page
from .quantization_ada import quantization_ada_page
from .quantization_hopper import quantization_hopper_page
from .quantization_blackwell import quantization_blackwell_page

__all__ = [
    "home_page",
    "quantization_page",
    "quantization_ampere_page",
    "quantization_ada_page",
    "quantization_hopper_page",
    "quantization_blackwell_page",
    "inference_page",
    "performance_page",
    "contact_page",
]
