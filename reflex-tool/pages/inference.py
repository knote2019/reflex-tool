"""Inference page."""
import reflex as rx
from ..components.navbar import navbar
from .. import State


def inference_page() -> rx.Component:
    """Inference page."""
    return rx.hstack(
        navbar(),
        rx.box(
            rx.container(
                rx.vstack(
                    # Title section - top
                    rx.heading(
                        "Model Inference",
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
                            href="/inference/ampere",
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
                            href="/inference/ada",
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
                            href="/inference/hopper",
                        ),
                        rx.link(
                            rx.button(
                                rx.hstack(
                                    rx.icon(tag="microchip", size=18, color="#EC4899"),
                                    rx.text("Blackwell"),
                                    spacing="2",
                                ),
                                variant="outline",
                                size="2",
                            ),
                            href="/inference/blackwell",
                        ),
                        spacing="3",
                        margin_bottom="0.75rem",
                        padding="0.75rem",
                        border_radius="0.5rem",
                        background="rgba(118, 185, 0, 0.05)",
                        width="100%",
                    ),
                    # TensorRT-LLM links container
                    rx.box(
                        rx.vstack(
                            rx.hstack(
                                rx.icon(tag="zap", size=18, color="#76B900"),
                                rx.text(
                                    "TensorRT-LLM",
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
                                    href="https://github.com/NVIDIA/TensorRT-LLM",
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
                                    href="https://nvidia.github.io/TensorRT-LLM/",
                                    is_external=True,
                                    _hover={
                                        "opacity": "0.8",
                                    },
                                ),
                                rx.text("•", color="#76B900", font_size="0.9rem"),
                                rx.link(
                                    rx.hstack(
                                        rx.icon(tag="box", size=16, color="#76B900"),
                                        rx.text(
                                            "NGC Container",
                                            font_size="0.9rem",
                                            color="#76B900",
                                        ),
                                        rx.icon(tag="external_link", size=14, color="#76B900"),
                                        spacing="2",
                                        align="center",
                                    ),
                                    href="https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tensorrt-llm/containers/release/",
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
                        margin_bottom="1.5rem",
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
