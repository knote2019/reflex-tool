"""Blackwell Architecture Inference page."""
import reflex as rx
from ..components.navbar import navbar
from .. import State


def inference_blackwell_page() -> rx.Component:
    """Blackwell Architecture Inference page."""
    return rx.hstack(
        navbar(),
        rx.box(
            rx.container(
                rx.vstack(
                    # Title
                    rx.heading(
                        "Blackwell Architecture - Model Inference",
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
                        href="/inference",
                    ),
                    # Architecture info
                    rx.box(
                        rx.vstack(
                            rx.heading(
                                "Blackwell GPUs",
                                font_size="1.2rem",
                                color="#F97316",
                                margin_bottom="0.5rem",
                            ),
                            rx.hstack(
                                rx.badge("B100", color_scheme="orange", variant="soft", size="2"),
                                rx.badge("B200", color_scheme="orange", variant="soft", size="2"),
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
                            on_change=State.set_modelopt_version,
                            size="2",
                            width="150px",
                        ),
                        rx.text(
                            "CPU Arch:",
                            font_weight="500",
                            font_size="0.95rem",
                            margin_left="2rem",
                        ),
                        rx.select(
                            [
                                "x86_64",
                                "aarch64",
                            ],
                            placeholder="Select CPU architecture",
                            value=State.selected_cpu_arch,
                            on_change=State.set_cpu_arch,
                            size="2",
                            width="150px",
                        ),
                        spacing="3",
                        align="center",
                        margin_bottom="0.5rem",
                    ),
                    # Inference Performance section
                    rx.box(
                        rx.vstack(
                            rx.hstack(
                                rx.icon(tag="activity", size=32, color="#F97316"),
                                rx.heading(
                                    "Inference Performance",
                                    font_size="1.3rem",
                                ),
                                spacing="2",
                                align="center",
                                margin_bottom="1rem",
                                width="100%",
                            ),
                            rx.text(
                                "Coming Soon: Inference performance metrics and benchmarks for Blackwell architecture.",
                                color="#666666",
                                font_size="0.95rem",
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

