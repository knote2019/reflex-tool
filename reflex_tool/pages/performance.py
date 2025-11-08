"""Performance page."""
import reflex as rx
from ..components.navbar import navbar


def performance_page() -> rx.Component:
    """Performance page."""
    return rx.hstack(
        navbar(),
        rx.box(
            rx.container(
                rx.vstack(
                    # Title section - top
                    rx.heading(
                        "Performance Optimization",
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
                                    rx.icon(tag="microchip", size=18, color="#667eea"),
                                    rx.text("Ampere"),
                                    spacing="2",
                                ),
                                variant="soft",
                                size="2",
                                color_scheme="green",
                            ),
                            href="/performance/ampere",
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
                            href="/performance/ada",
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
                            href="/performance/hopper",
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
                            href="/performance/blackwell",
                        ),
                        spacing="3",
                        margin_bottom="0.75rem",
                        padding="0.75rem",
                        border_radius="0.5rem",
                        background="rgba(102, 126, 234, 0.05)",
                        width="100%",
                    ),
                    # trtllm-bench documentation link
                    rx.box(
                        rx.vstack(
                            rx.hstack(
                                rx.icon(tag="gauge", size=18, color="#667eea"),
                                rx.text(
                                    "trtllm-bench",
                                    font_size="1rem",
                                    font_weight="600",
                                    color="#1F2937",
                                ),
                                spacing="2",
                                align="center",
                            ),
                            rx.link(
                                rx.hstack(
                                    rx.icon(tag="book_open", size=16, color="#667eea"),
                                    rx.text(
                                        "Benchmarking Documentation",
                                        font_size="0.9rem",
                                        color="#667eea",
                                    ),
                                    rx.icon(tag="external_link", size=14, color="#667eea"),
                                    spacing="2",
                                    align="center",
                                ),
                                href="https://nvidia.github.io/TensorRT-LLM/commands/trtllm-bench.html",
                                is_external=True,
                                _hover={
                                    "opacity": "0.8",
                                },
                            ),
                            spacing="3",
                            align="start",
                        ),
                        padding="1rem",
                        border_radius="0.5rem",
                        border="1px solid rgba(102, 126, 234, 0.3)",
                        background="rgba(102, 126, 234, 0.05)",
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
