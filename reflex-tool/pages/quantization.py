"""Quantization page."""
import reflex as rx
from ..components.navbar import navbar
from .. import State


def status_icon(model: str, quantization_format: str) -> rx.Component:
    """Return the appropriate status icon based on test status."""
    status_key = f"{model}_{quantization_format}"
    
    # Get the status value, default to "passed" if not found
    status_value = State.test_status.get(status_key, "passed")
    
    return rx.match(
        status_value,
        ("passed", rx.icon(tag="circle_check", size=20, color="#76B900")),
        ("failed", rx.icon(tag="circle_alert", size=20, color="#FFB900")),
        ("unsupported", rx.icon(tag="circle_x", size=20, color="#999999")),
        rx.icon(tag="circle_check", size=20, color="#76B900"),  # default
    )


def download_cell(model: str, quantization_format: str) -> rx.Component:
    """Create a cell with status icon and download button."""
    return rx.table.cell(
        rx.hstack(
            # Status icon
            status_icon(model, quantization_format),
            # Download button
            rx.button(
                rx.icon(tag="download", size=18),
                on_click=lambda: State.download_log(model, quantization_format),
                background="transparent",
                border="none",
                cursor="pointer",
                _hover={"background": "#f0f0f0", "transform": "scale(1.1)"},
                padding="0.3rem",
                color="#666666",
            ),
            spacing="2",
            align="center",
            justify="center",
        ),
        text_align="center",
    )


def quantization_page() -> rx.Component:
    """Quantization page."""
    return rx.hstack(
        navbar(),
        rx.box(
        rx.container(
            rx.vstack(
                # Title section - top
                rx.heading(
                    "Model Quantization",
                    font_size="1.8rem",
                    font_weight="600",
                    margin_top="1.5rem",
                        margin_bottom="1rem",
                ),
                    # GPU Type Sub-navigation
                    rx.hstack(
                        rx.link(
                            rx.button(
                                rx.hstack(
                                    rx.icon(tag="microchip", size=18, color="#76B900"),
                                    rx.text("Ampere"),
                                    spacing="2",
                                ),
                                variant="soft",
                                size="2",
                                color_scheme="green",
                            ),
                            href="/quantization/ampere",
                        ),
                        rx.link(
                            rx.button(
                                rx.hstack(
                                    rx.icon(tag="microchip", size=18, color="#3B82F6"),
                                    rx.text("Ada"),
                                    spacing="2",
                                ),
                                variant="outline",
                                size="2",
                            ),
                            href="/quantization/ada",
                        ),
                        rx.link(
                            rx.button(
                                rx.hstack(
                                    rx.icon(tag="microchip", size=18, color="#A855F7"),
                                    rx.text("Hopper"),
                                    spacing="2",
                                ),
                                variant="outline",
                                size="2",
                            ),
                            href="/quantization/hopper",
                        ),
                        rx.link(
                            rx.button(
                                rx.hstack(
                                    rx.icon(tag="microchip", size=18, color="#F97316"),
                                    rx.text("Blackwell"),
                                    spacing="2",
                                ),
                                variant="outline",
                                size="2",
                            ),
                            href="/quantization/blackwell",
                        ),
                        spacing="3",
                        margin_bottom="1.5rem",
                        padding="0.75rem",
                        border_radius="0.5rem",
                        background="rgba(118, 185, 0, 0.05)",
                        width="100%",
                    ),
                    # ModelOpt version selection
                    rx.hstack(
                        rx.text(
                            "ModelOpt Version:",
                            font_weight="500",
                            font_size="0.95rem",
                        ),
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
                            width="150px",
                        ),
                        spacing="3",
                        align="center",
                        margin_bottom="0.5rem",
                    ),
                    # Configuration section
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
                                        download_cell("Llama-3.1-8B-Instruct", "fp8"),
                                        download_cell("Llama-3.1-8B-Instruct", "int8_sq"),
                                        download_cell("Llama-3.1-8B-Instruct", "int4_awq"),
                                        download_cell("Llama-3.1-8B-Instruct", "w4a8_awq"),
                                        download_cell("Llama-3.1-8B-Instruct", "nvfp4"),
                                    ),
                                    rx.table.row(
                                        rx.table.cell("Llama-3.3-70B-Instruct", font_weight="500"),
                                        download_cell("Llama-3.3-70B-Instruct", "fp8"),
                                        download_cell("Llama-3.3-70B-Instruct", "int8_sq"),
                                        download_cell("Llama-3.3-70B-Instruct", "int4_awq"),
                                        download_cell("Llama-3.3-70B-Instruct", "w4a8_awq"),
                                        download_cell("Llama-3.3-70B-Instruct", "nvfp4"),
                                    ),
                                    rx.table.row(
                                        rx.table.cell("Llama-4-Scout-17B-16E-Instruct", font_weight="500"),
                                        download_cell("Llama-4-Scout-17B-16E-Instruct", "fp8"),
                                        download_cell("Llama-4-Scout-17B-16E-Instruct", "int8_sq"),
                                        download_cell("Llama-4-Scout-17B-16E-Instruct", "int4_awq"),
                                        download_cell("Llama-4-Scout-17B-16E-Instruct", "w4a8_awq"),
                                        download_cell("Llama-4-Scout-17B-16E-Instruct", "nvfp4"),
                                    ),
                                    rx.table.row(
                                        rx.table.cell("Llama-4-Maverick-17B-128E-Instruct", font_weight="500"),
                                        download_cell("Llama-4-Maverick-17B-128E-Instruct", "fp8"),
                                        download_cell("Llama-4-Maverick-17B-128E-Instruct", "int8_sq"),
                                        download_cell("Llama-4-Maverick-17B-128E-Instruct", "int4_awq"),
                                        download_cell("Llama-4-Maverick-17B-128E-Instruct", "w4a8_awq"),
                                        download_cell("Llama-4-Maverick-17B-128E-Instruct", "nvfp4"),
                                    ),
                                    rx.table.row(
                                        rx.table.cell("Mixtral-8x7B-Instruct-v0.1", font_weight="500"),
                                        download_cell("Mixtral-8x7B-Instruct-v0.1", "fp8"),
                                        download_cell("Mixtral-8x7B-Instruct-v0.1", "int8_sq"),
                                        download_cell("Mixtral-8x7B-Instruct-v0.1", "int4_awq"),
                                        download_cell("Mixtral-8x7B-Instruct-v0.1", "w4a8_awq"),
                                        download_cell("Mixtral-8x7B-Instruct-v0.1", "nvfp4"),
                                    ),
                                    rx.table.row(
                                        rx.table.cell("Mixtral-8x22B-Instruct-v0.1", font_weight="500"),
                                        download_cell("Mixtral-8x22B-Instruct-v0.1", "fp8"),
                                        download_cell("Mixtral-8x22B-Instruct-v0.1", "int8_sq"),
                                        download_cell("Mixtral-8x22B-Instruct-v0.1", "int4_awq"),
                                        download_cell("Mixtral-8x22B-Instruct-v0.1", "w4a8_awq"),
                                        download_cell("Mixtral-8x22B-Instruct-v0.1", "nvfp4"),
                                    ),
                                    rx.table.row(
                                        rx.table.cell("Phi-3-medium-4k-instruct", font_weight="500"),
                                        download_cell("Phi-3-medium-4k-instruct", "fp8"),
                                        download_cell("Phi-3-medium-4k-instruct", "int8_sq"),
                                        download_cell("Phi-3-medium-4k-instruct", "int4_awq"),
                                        download_cell("Phi-3-medium-4k-instruct", "w4a8_awq"),
                                        download_cell("Phi-3-medium-4k-instruct", "nvfp4"),
                                    ),
                                    rx.table.row(
                                        rx.table.cell("Phi-4", font_weight="500"),
                                        download_cell("Phi-4", "fp8"),
                                        download_cell("Phi-4", "int8_sq"),
                                        download_cell("Phi-4", "int4_awq"),
                                        download_cell("Phi-4", "w4a8_awq"),
                                        download_cell("Phi-4", "nvfp4"),
                                    ),
                                    rx.table.row(
                                        rx.table.cell("Llama-3_3-Nemotron-Super-49B-v1", font_weight="500"),
                                        download_cell("Llama-3_3-Nemotron-Super-49B-v1", "fp8"),
                                        download_cell("Llama-3_3-Nemotron-Super-49B-v1", "int8_sq"),
                                        download_cell("Llama-3_3-Nemotron-Super-49B-v1", "int4_awq"),
                                        download_cell("Llama-3_3-Nemotron-Super-49B-v1", "w4a8_awq"),
                                        download_cell("Llama-3_3-Nemotron-Super-49B-v1", "nvfp4"),
                                    ),
                                    rx.table.row(
                                        rx.table.cell("Llama-3_1-Nemotron-Ultra-253B-v1", font_weight="500"),
                                        download_cell("Llama-3_1-Nemotron-Ultra-253B-v1", "fp8"),
                                        download_cell("Llama-3_1-Nemotron-Ultra-253B-v1", "int8_sq"),
                                        download_cell("Llama-3_1-Nemotron-Ultra-253B-v1", "int4_awq"),
                                        download_cell("Llama-3_1-Nemotron-Ultra-253B-v1", "w4a8_awq"),
                                        download_cell("Llama-3_1-Nemotron-Ultra-253B-v1", "nvfp4"),
                                    ),
                                    rx.table.row(
                                        rx.table.cell("Qwen2-7B-Instruct", font_weight="500"),
                                        download_cell("Qwen2-7B-Instruct", "fp8"),
                                        download_cell("Qwen2-7B-Instruct", "int8_sq"),
                                        download_cell("Qwen2-7B-Instruct", "int4_awq"),
                                        download_cell("Qwen2-7B-Instruct", "w4a8_awq"),
                                        download_cell("Qwen2-7B-Instruct", "nvfp4"),
                                    ),
                                    rx.table.row(
                                        rx.table.cell("Qwen2.5-72B-Instruct", font_weight="500"),
                                        download_cell("Qwen2.5-72B-Instruct", "fp8"),
                                        download_cell("Qwen2.5-72B-Instruct", "int8_sq"),
                                        download_cell("Qwen2.5-72B-Instruct", "int4_awq"),
                                        download_cell("Qwen2.5-72B-Instruct", "w4a8_awq"),
                                        download_cell("Qwen2.5-72B-Instruct", "nvfp4"),
                                    ),
                                    rx.table.row(
                                        rx.table.cell("Qwen3-30B-A3B", font_weight="500"),
                                        download_cell("Qwen3-30B-A3B", "fp8"),
                                        download_cell("Qwen3-30B-A3B", "int8_sq"),
                                        download_cell("Qwen3-30B-A3B", "int4_awq"),
                                        download_cell("Qwen3-30B-A3B", "w4a8_awq"),
                                        download_cell("Qwen3-30B-A3B", "nvfp4"),
                                    ),
                                    rx.table.row(
                                        rx.table.cell("Qwen3-235B-A22B-Thinking-2507", font_weight="500"),
                                        download_cell("Qwen3-235B-A22B-Thinking-2507", "fp8"),
                                        download_cell("Qwen3-235B-A22B-Thinking-2507", "int8_sq"),
                                        download_cell("Qwen3-235B-A22B-Thinking-2507", "int4_awq"),
                                        download_cell("Qwen3-235B-A22B-Thinking-2507", "w4a8_awq"),
                                        download_cell("Qwen3-235B-A22B-Thinking-2507", "nvfp4"),
                                    ),
                                    rx.table.row(
                                        rx.table.cell("Qwen3-Next-80B-A3B-Thinking", font_weight="500"),
                                        download_cell("Qwen3-Next-80B-A3B-Thinking", "fp8"),
                                        download_cell("Qwen3-Next-80B-A3B-Thinking", "int8_sq"),
                                        download_cell("Qwen3-Next-80B-A3B-Thinking", "int4_awq"),
                                        download_cell("Qwen3-Next-80B-A3B-Thinking", "w4a8_awq"),
                                        download_cell("Qwen3-Next-80B-A3B-Thinking", "nvfp4"),
                                    ),
                                    rx.table.row(
                                        rx.table.cell("QwQ-32B", font_weight="500"),
                                        download_cell("QwQ-32B", "fp8"),
                                        download_cell("QwQ-32B", "int8_sq"),
                                        download_cell("QwQ-32B", "int4_awq"),
                                        download_cell("QwQ-32B", "w4a8_awq"),
                                        download_cell("QwQ-32B", "nvfp4"),
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
            margin_left="250px",
            width="100%",
        ),
        spacing="0",
        align="start",
    )
