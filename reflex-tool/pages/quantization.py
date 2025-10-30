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
