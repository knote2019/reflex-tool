"""Inference page."""
import reflex as rx
from ..components.navbar import navbar


def inference_page() -> rx.Component:
    """Inference page."""
    return rx.box(
        navbar(),
        rx.container(
            rx.vstack(
                rx.heading(
                    "Model Inference",
                    font_size="2.5rem",
                    margin_top="3rem",
                ),
                rx.text(
                    "Efficient model inference engine supporting multiple deep learning frameworks, providing fast and stable inference services.",
                    font_size="1.1rem",
                    color="gray.700",
                    margin_top="1.5rem",
                    line_height="1.8",
                ),
                rx.text(
                    "Inference Engine Features:",
                    font_size="1.1rem",
                    font_weight="bold",
                    margin_top="2rem",
                ),
                rx.unordered_list(
                    rx.list_item("Support for multiple frameworks: PyTorch, TensorFlow, ONNX"),
                    rx.list_item("Batch processing optimization to improve throughput"),
                    rx.list_item("GPU/CPU hybrid scheduling for maximum resource utilization"),
                    rx.list_item("Low-latency inference with millisecond response times"),
                    font_size="1.1rem",
                    color="gray.700",
                    spacing="3",
                    margin_top="1rem",
                ),
                spacing="4",
                padding="2rem",
                align="start",
            ),
            max_width="800px",
        ),
    )
