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
                # Title section - top
                rx.heading(
                    "Model Quantization",
                    font_size="1.8rem",
                    font_weight="600",
                    margin_top="1.5rem",
                    margin_bottom="1.5rem",
                ),
                # Configuration section
                rx.hstack(
                    # GPU selection
                    rx.box(
                        rx.vstack(
                            rx.heading(
                                "Select GPU",
                                font_size="1.3rem",
                                margin_bottom="1rem",
                            ),
                            rx.select(
                                [
                                    "H200",
                                    "GH200",
                                    "B100",
                                    "B200",
                                    "GB200",
                                ],
                                placeholder="Select a GPU",
                                value=State.selected_gpu,
                                on_change=State.set_gpu,
                                size="3",
                                width="100%",
                            ),
                            rx.text(
                                f"Selected: {State.selected_gpu}",
                                font_size="0.9rem",
                                color="gray.600",
                                margin_top="1rem",
                            ),
                            align="start",
                            width="100%",
                        ),
                        padding="1.5rem",
                        border_radius="1rem",
                        box_shadow="0 4px 6px rgba(0, 0, 0, 0.1)",
                        background="white",
                        width="350px",
                        height="fit-content",
                    ),
                    # Model selection
                    rx.box(
                        rx.vstack(
                            rx.heading(
                                "Select Model",
                                font_size="1.3rem",
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
                                font_size="0.9rem",
                                color="gray.600",
                                margin_top="1rem",
                            ),
                            align="start",
                            width="100%",
                        ),
                        padding="1.5rem",
                        border_radius="1rem",
                        box_shadow="0 4px 6px rgba(0, 0, 0, 0.1)",
                        background="white",
                        width="350px",
                        height="fit-content",
                    ),
                    # Quantization format selection
                    rx.box(
                        rx.vstack(
                            rx.heading(
                                "Select QFormat",
                                font_size="1.3rem",
                                margin_bottom="1rem",
                            ),
                            rx.select(
                                [
                                    "fp8",
                                    "int8_sq",
                                    "int4_awq",
                                    "w4a8_awq",
                                    "nvfp4",
                                ],
                                placeholder="Select quantization format",
                                value=State.selected_quantization,
                                on_change=State.set_quantization,
                                size="3",
                                width="100%",
                            ),
                            rx.text(
                                f"Selected: {State.selected_quantization}",
                                font_size="0.9rem",
                                color="gray.600",
                                margin_top="1rem",
                            ),
                            align="start",
                            width="100%",
                        ),
                        padding="1.5rem",
                        border_radius="1rem",
                        box_shadow="0 4px 6px rgba(0, 0, 0, 0.1)",
                        background="white",
                        width="350px",
                        height="fit-content",
                    ),
                    spacing="4",
                    align="start",
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
