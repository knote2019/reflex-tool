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
                    # TensorRT Model Optimizer Links
                    rx.box(
                        rx.vstack(
                            rx.hstack(
                                rx.icon(tag="wrench", size=18, color="#76B900"),
                                rx.text(
                                    "NVIDIA Model Optimizer",
                                    font_size="1rem",
                                    font_weight="600",
                                    color="#1F2937",
                                ),
                                spacing="2",
                                align="center",
                            ),
                            rx.hstack(
                                rx.link(
                                    rx.hstack(
                                        rx.icon(tag="github", size=16, color="#76B900"),
                                        rx.text(
                                            "GitHub",
                                            font_size="0.9rem",
                                            color="#76B900",
                                        ),
                                        rx.icon(tag="external_link", size=14, color="#76B900"),
                                        spacing="2",
                                        align="center",
                                    ),
                                    href="https://github.com/NVIDIA/TensorRT-Model-Optimizer",
                                    is_external=True,
                                    _hover={
                                        "opacity": "0.8",
                                    },
                                ),
                                rx.text("•", color="#76B900", font_size="0.9rem"),
                                rx.link(
                                    rx.hstack(
                                        rx.icon(tag="book_open", size=16, color="#76B900"),
                                        rx.text(
                                            "Documentation",
                                            font_size="0.9rem",
                                            color="#76B900",
                                        ),
                                        rx.icon(tag="external_link", size=14, color="#76B900"),
                                        spacing="2",
                                        align="center",
                                    ),
                                    href="https://nvidia.github.io/TensorRT-Model-Optimizer/",
                                    is_external=True,
                                    _hover={
                                        "opacity": "0.8",
                                    },
                                ),
                                spacing="3",
                                align="center",
                            ),
                            spacing="3",
                            align="start",
                        ),
                        padding="1rem",
                        border_radius="0.5rem",
                        border="1px solid rgba(118, 185, 0, 0.3)",
                        background="rgba(118, 185, 0, 0.05)",
                        margin_top="3rem",
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
