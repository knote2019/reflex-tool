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
from .inference_ampere import inference_ampere_page
from .inference_ada import inference_ada_page
from .inference_hopper import inference_hopper_page
from .inference_blackwell import inference_blackwell_page

__all__ = [
    "home_page",
    "quantization_page",
    "quantization_ampere_page",
    "quantization_ada_page",
    "quantization_hopper_page",
    "quantization_blackwell_page",
    "inference_page",
    "inference_ampere_page",
    "inference_ada_page",
    "inference_hopper_page",
    "inference_blackwell_page",
    "performance_page",
    "contact_page",
]
