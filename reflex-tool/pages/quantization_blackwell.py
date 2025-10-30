"""Blackwell Architecture page."""
import reflex as rx
from ..components.navbar import navbar
from .. import State


def download_cell(model: str, quantization_format: str) -> rx.Component:
    """Create a cell with status icon and download button."""
    status_key = f"{model}_{quantization_format}"
    status_value = State.test_status.get(status_key, "passed")
    
    return rx.table.cell(
        rx.hstack(
            rx.match(
                status_value,
                ("passed", rx.icon(tag="circle_check", size=20, color="#76B900")),
                ("failed", rx.icon(tag="circle_alert", size=20, color="#FFB900")),
                ("unsupported", rx.icon(tag="circle_x", size=20, color="#999999")),
                rx.icon(tag="circle_check", size=20, color="#76B900"),
            ),
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


def quantization_blackwell_page() -> rx.Component:
    """Blackwell Architecture page."""
    return rx.hstack(
        navbar(),
        rx.box(
            rx.container(
                rx.vstack(
                    rx.heading(
                        "Blackwell Architecture - Model Quantization",
                        font_size="1.8rem",
                        font_weight="600",
                        margin_top="1.5rem",
                        margin_bottom="1rem",
                    ),
                    # Back button
                    rx.link(
                        rx.button(
                            rx.hstack(
                                rx.icon(tag="arrow_left", size=18),
                                rx.text("Back to Overview"),
                                spacing="2",
                            ),
                            variant="outline",
                            size="2",
                        ),
                        href="/quantization",
                    ),
                    # Architecture info
                    rx.box(
                        rx.vstack(
                            rx.heading(
                                "Blackwell Architecture",
                                font_size="1.2rem",
                                color="#F97316",
                                margin_bottom="0.5rem",
                            ),
                            rx.text(
                                "Available GPU models:",
                                font_size="0.9rem",
                                color="gray.700",
                                margin_bottom="0.5rem",
                            ),
                            rx.hstack(
                                rx.badge("B100", color_scheme="orange", variant="soft", size="2"),
                                rx.badge("B200", color_scheme="orange", variant="soft", size="2"),
                                rx.badge("GB100", color_scheme="orange", variant="soft", size="2"),
                                rx.badge("GB200", color_scheme="orange", variant="soft", size="2"),
                                spacing="2",
                                wrap="wrap",
                            ),
                        ),
                        padding="1rem",
                        border_radius="0.5rem",
                        background="rgba(249, 115, 22, 0.05)",
                        border="1px solid rgba(249, 115, 22, 0.2)",
                        margin_bottom="1rem",
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
                    # Model & Quantization Format table
                    rx.box(
                        rx.vstack(
                            rx.hstack(
                                rx.icon(tag="layers", size=32, color="#F97316"),
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
                                        rx.table.column_header_cell("int4_awq"),
                                        rx.table.column_header_cell("nvfp4"),
                                    ),
                                ),
                                rx.table.body(
                                    rx.table.row(
                                        rx.table.cell("Qwen3-235B-A22B-Thinking-2507", font_weight="500"),
                                        download_cell("Qwen3-235B-A22B-Thinking-2507", "fp8"),
                                        download_cell("Qwen3-235B-A22B-Thinking-2507", "int4_awq"),
                                        download_cell("Qwen3-235B-A22B-Thinking-2507", "nvfp4"),
                                    ),
                                    rx.table.row(
                                        rx.table.cell("Qwen3-Next-80B-A3B-Thinking", font_weight="500"),
                                        download_cell("Qwen3-Next-80B-A3B-Thinking", "fp8"),
                                        download_cell("Qwen3-Next-80B-A3B-Thinking", "int4_awq"),
                                        download_cell("Qwen3-Next-80B-A3B-Thinking", "nvfp4"),
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
                        margin_top="1rem",
                        width="100%",
                        max_width="900px",
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

