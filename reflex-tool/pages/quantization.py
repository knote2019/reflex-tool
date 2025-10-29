"""Quantization page."""
import reflex as rx
from ..components.navbar import navbar
from .. import State


def quantization_page() -> rx.Component:
    """Quantization page."""
    return rx.box(
        navbar(),
        rx.container(
            rx.vstack(
                rx.heading(
                    "Model Quantization",
                    font_size="3rem",
                    margin_top="4rem",
                    text_align="center",
                ),
                rx.text(
                    "Efficient model quantization techniques to reduce model size and improve inference speed",
                    font_size="1.2rem",
                    color="gray.600",
                    text_align="center",
                    margin_top="1rem",
                ),
                # Model selection section
                rx.box(
                    rx.vstack(
                        rx.heading(
                            "Select Model",
                            font_size="1.5rem",
                            margin_bottom="1rem",
                        ),
                        rx.select(
                            [
                                "Llama-3.1-8B-Instruct",
                                "Llama-3.3-70B-Instruct",
                                "Qwen2-7B-Instruct",
                                "Qwen2.5-72B-Instruct",
                            ],
                            placeholder="Select a model",
                            value=State.selected_model,
                            on_change=State.set_model,
                            size="3",
                            width="100%",
                        ),
                        rx.text(
                            f"Selected: {State.selected_model}",
                            font_size="1rem",
                            color="gray.600",
                            margin_top="1rem",
                        ),
                        align="start",
                        width="100%",
                    ),
                    padding="2rem",
                    border_radius="1rem",
                    box_shadow="0 4px 6px rgba(0, 0, 0, 0.1)",
                    background="white",
                    margin_top="3rem",
                    width="100%",
                    max_width="600px",
                ),
                rx.hstack(
                    rx.box(
                        rx.icon(tag="zap", size=48, color="#76B900"),
                        rx.heading("INT8 Quantization", font_size="1.5rem", margin_top="1rem"),
                        rx.text(
                            "Reduce model precision to 8-bit integers, significantly reducing model size",
                            color="gray.600",
                            text_align="center",
                        ),
                        padding="2rem",
                        border_radius="1rem",
                        box_shadow="0 4px 6px rgba(0, 0, 0, 0.1)",
                        width="300px",
                    ),
                    rx.box(
                        rx.icon(tag="layers", size=48, color="#76B900"),
                        rx.heading("Dynamic Quantization", font_size="1.5rem", margin_top="1rem"),
                        rx.text(
                            "Runtime dynamic quantization, balancing accuracy and performance",
                            color="gray.600",
                            text_align="center",
                        ),
                        padding="2rem",
                        border_radius="1rem",
                        box_shadow="0 4px 6px rgba(0, 0, 0, 0.1)",
                        width="300px",
                    ),
                    rx.box(
                        rx.icon(tag="sparkles", size=48, color="#76B900"),
                        rx.heading("Mixed Precision", font_size="1.5rem", margin_top="1rem"),
                        rx.text(
                            "Use different precision for different layers to optimize performance",
                            color="gray.600",
                            text_align="center",
                        ),
                        padding="2rem",
                        border_radius="1rem",
                        box_shadow="0 4px 6px rgba(0, 0, 0, 0.1)",
                        width="300px",
                    ),
                    spacing="4",
                    margin_top="3rem",
                    wrap="wrap",
                    justify="center",
                ),
                spacing="4",
                padding="2rem",
            ),
            max_width="1200px",
        ),
    )
