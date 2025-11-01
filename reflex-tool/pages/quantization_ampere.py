"""Ampere Architecture page."""
import reflex as rx
from ..components.navbar import navbar
from .. import State


def status_icon_cell(model: str, qformat: str) -> rx.Component:
    """Create a table cell with status icon and download button."""
    status_key = f"{model}_{qformat}"
    
    return rx.table.cell(
        rx.hstack(
            rx.cond(
                State.test_status.get(status_key, "NA") == "passed",
                rx.icon(tag="circle_check", size=20, color="#76B900"),
                rx.cond(
                    State.test_status.get(status_key, "NA") == "failed",
                    rx.icon(tag="circle_alert", size=20, color="#FFB900"),
                    rx.cond(
                        State.test_status.get(status_key, "NA") == "unsupported",
                        rx.icon(tag="circle_x", size=20, color="#999999"),
                        rx.icon(tag="circle_minus", size=20, color="#999999"),
                    ),
                ),
            ),
            rx.button(
                rx.icon(tag="download", size=18),
                on_click=lambda: State.download_log(model, qformat),
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


def quantization_ampere_page() -> rx.Component:
    """Ampere Architecture page."""
    return rx.hstack(
        navbar(),
        rx.box(
            rx.container(
                rx.vstack(
                    # Title
                    rx.heading(
                        "Ampere Architecture - Model Quantization",
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
                                "Ampere GPUs",
                                font_size="1.2rem",
                                color="#76B900",
                                margin_bottom="0.5rem",
                            ),
                            rx.hstack(
                                rx.badge("A100", color_scheme="green", variant="soft", size="2"),
                                spacing="2",
                                wrap="wrap",
                            ),
                        ),
                        padding="1rem",
                        border_radius="0.5rem",
                        background="rgba(118, 185, 0, 0.05)",
                        border="1px solid rgba(118, 185, 0, 0.2)",
                        margin_bottom="1rem",
                        width="100%",
                    ),
                    # ModelOpt version and CPU architecture selection
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
                            on_change=State.set_modelopt_version_and_reload_ampere,
                            size="2",
                            width="150px",
                        ),
                        rx.text(
                            "GPU Name:",
                            font_weight="500",
                            font_size="0.95rem",
                            margin_left="2rem",
                        ),
                        rx.select(
                            [
                                "A100",
                            ],
                            placeholder="Select CPU architecture",
                            value=State.selected_cpu_arch,
                            on_change=State.set_cpu_arch_and_reload_ampere,
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
                                rx.icon(tag="layers", size=32, color="#76B900"),
                                rx.heading(
                                    "Model & Quantization Format",
                                    font_size="1.3rem",
                                ),
                                rx.spacer(),
                                rx.button(
                                    rx.icon(tag="refresh_cw", size=18),
                                    "refresh",
                                    on_click=State.refresh_ampere_data,
                                    variant="outline",
                                    size="2",
                                    color_scheme="green",
                                ),
                                spacing="2",
                                align="center",
                                margin_bottom="1rem",
                                width="100%",
                            ),
                            rx.table.root(
                                rx.table.header(
                                    rx.table.row(
                                        rx.table.column_header_cell("Model"),
                                        rx.foreach(
                                            State.ampere_quantization_formats,
                                            lambda qformat: rx.table.column_header_cell(qformat),
                                        ),
                                    ),
                                ),
                                rx.table.body(
                                    rx.foreach(
                                        State.ampere_test_models,
                                        lambda model: rx.table.row(
                                            rx.table.cell(model, font_weight="500"),
                                            rx.foreach(
                                                State.ampere_quantization_formats,
                                                lambda qformat: status_icon_cell(model, qformat),
                                            ),
                                        ),
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
                    on_mount=State.load_ampere_data,
                ),
                max_width="1200px",
            ),
            margin_left="250px",
            width="100%",
        ),
        spacing="0",
        align="start",
    )
