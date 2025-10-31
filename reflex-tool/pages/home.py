"""Home page."""
import reflex as rx
from ..components.navbar import navbar


def home_page() -> rx.Component:
    """Home page."""
    return rx.hstack(
        navbar(),
        rx.box(
            rx.container(
                rx.vstack(
                    rx.heading(
                        "Welcome to NVIDIA Model Optimizer",
                        font_size="2.5rem",
                        margin_top="3rem",
                        text_align="center",
                    ),
                # GitHub Repository Link
                rx.box(
                    rx.link(
                        rx.hstack(
                            rx.icon(tag="github", size=24, color="#333"),
                            rx.text(
                                "NVIDIA/TensorRT-Model-Optimizer",
                                font_size="1.1rem",
                                font_weight="500",
                                color="#333",
                            ),
                            rx.icon(tag="external_link", size=20, color="#666"),
                            spacing="3",
                            align="center",
                        ),
                        href="https://github.com/NVIDIA/TensorRT-Model-Optimizer",
                        is_external=True,
                        _hover={
                            "opacity": "0.8",
                        },
                    ),
                    padding="1.5rem 2rem",
                    border_radius="0.75rem",
                    background="linear-gradient(135deg, rgba(118, 185, 0, 0.05) 0%, rgba(255, 255, 255, 1) 100%)",
                    border="1px solid rgba(118, 185, 0, 0.2)",
                    margin_top="3rem",
                    _hover={
                        "border_color": "rgba(118, 185, 0, 0.4)",
                        "box_shadow": "0 4px 12px rgba(118, 185, 0, 0.15)",
                    },
                    transition="all 0.2s ease-in-out",
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

