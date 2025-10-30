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
                    # ModelOpt and GPU table
                    rx.box(
                        rx.vstack(
                            rx.hstack(
                                rx.icon(tag="zap", size=32, color="#76B900"),
                            rx.heading(
                                    "Environment Setup",
                                font_size="1.3rem",
                                ),
                                spacing="2",
                                align="center",
                                margin_bottom="1rem",
                            ),
                            rx.table.root(
                                rx.table.header(
                                    rx.table.row(
                                        rx.table.column_header_cell("Configuration"),
                                        rx.table.column_header_cell("Selection"),
                                    ),
                                ),
                                rx.table.body(
                                    rx.table.row(
                                        rx.table.cell("ModelOpt", font_weight="500"),
                                        rx.table.cell(
                                            rx.select(
                                                [
                                                    "0.39.0",
                                                    "0.40.0",
                                                    "0.42.0",
                                                ],
                                                placeholder="Select version",
                                                value=State.selected_modelopt_version,
                                                on_change=State.set_modelopt_version,
                                                size="2",
                                                width="100%",
                                            ),
                                        ),
                                    ),
                                    rx.table.row(
                                        rx.table.cell("GPU", font_weight="500"),
                                        rx.table.cell(
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
                                                size="2",
                                width="100%",
                            ),
                                        ),
                                    ),
                                ),
                                width="100%",
                            ),
                            rx.text(
                                f"Selected: {State.selected_modelopt_version} | {State.selected_gpu}",
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
                        width="500px",
                        height="fit-content",
                    ),
                    spacing="4",
                    align="start",
                ),
                # Model and Quantization Format table
                rx.box(
                    rx.vstack(
                        rx.hstack(
                            rx.icon(tag="layers", size=32, color="#76B900"),
                        rx.heading(
                                "Model & Quantization Format",
                            font_size="1.3rem",
                            ),
                            spacing="2",
                            align="center",
                            margin_bottom="1rem",
                        ),
                        rx.table.root(
                            rx.table.header(
                                rx.table.row(
                                    rx.table.column_header_cell("Model"),
                                    rx.table.column_header_cell("fp8"),
                                    rx.table.column_header_cell("int8_sq"),
                                    rx.table.column_header_cell("int4_awq"),
                                    rx.table.column_header_cell("w4a8_awq"),
                                    rx.table.column_header_cell("nvfp4"),
                                ),
                            ),
                            rx.table.body(
                                rx.table.row(
                                    rx.table.cell("Llama-3.1-8B-Instruct", font_weight="500"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                ),
                                rx.table.row(
                                    rx.table.cell("Llama-3.3-70B-Instruct", font_weight="500"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                ),
                                rx.table.row(
                                    rx.table.cell("Llama-4-Scout-17B-16E-Instruct", font_weight="500"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                ),
                                rx.table.row(
                                    rx.table.cell("Llama-4-Maverick-17B-128E-Instruct", font_weight="500"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                ),
                                rx.table.row(
                                    rx.table.cell("Mixtral-8x7B-Instruct-v0.1", font_weight="500"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                ),
                                rx.table.row(
                                    rx.table.cell("Mixtral-8x22B-Instruct-v0.1", font_weight="500"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                ),
                                rx.table.row(
                                    rx.table.cell("Phi-3-medium-4k-instruct", font_weight="500"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                ),
                                rx.table.row(
                                    rx.table.cell("Phi-4", font_weight="500"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                ),
                                rx.table.row(
                                    rx.table.cell("Llama-3_3-Nemotron-Super-49B-v1", font_weight="500"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                ),
                                rx.table.row(
                                    rx.table.cell("Llama-3_1-Nemotron-Ultra-253B-v1", font_weight="500"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                ),
                                rx.table.row(
                                    rx.table.cell("Qwen2-7B-Instruct", font_weight="500"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                ),
                                rx.table.row(
                                    rx.table.cell("Qwen2.5-72B-Instruct", font_weight="500"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                ),
                                rx.table.row(
                                    rx.table.cell("Qwen3-30B-A3B", font_weight="500"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                ),
                                rx.table.row(
                                    rx.table.cell("Qwen3-235B-A22B-Thinking-2507", font_weight="500"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                ),
                                rx.table.row(
                                    rx.table.cell("Qwen3-Next-80B-A3B-Thinking", font_weight="500"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                ),
                                rx.table.row(
                                    rx.table.cell("QwQ-32B", font_weight="500"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                    rx.table.cell("✓", color="#76B900", font_size="1.2rem", text_align="center"),
                                ),
                            ),
                            width="100%",
                        ),
                        align="start",
                        width="100%",
                    ),
                    padding="1.5rem",
                    border_radius="1rem",
                    box_shadow="0 4px 6px rgba(0, 0, 0, 0.1)",
                    background="white",
                    margin_top="2rem",
                    width="100%",
                    max_width="900px",
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
