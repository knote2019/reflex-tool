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
                                    rx.icon(tag="microchip", size=18, color="#76B900"),
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
                                    rx.icon(tag="microchip", size=18, color="#D4A59A"),
                                    rx.text("Blackwell"),
                                    spacing="2",
                                ),
                                variant="outline",
                                size="2",
                            ),
                            href="/performance/blackwell",
                        ),
                        spacing="3",
                        margin_bottom="1.5rem",
                        padding="0.75rem",
                        border_radius="0.5rem",
                        background="rgba(118, 185, 0, 0.05)",
                        width="100%",
                    ),
                    # Performance overview content
                    rx.grid(
                        rx.box(
                            rx.icon(tag="activity", size=40, color="#76B900"),
                            rx.heading("Throughput Optimization", font_size="1.3rem", margin_top="1rem"),
                            rx.text(
                                "Batch processing and parallel computing to increase requests per time unit",
                                color="gray.600",
                                margin_top="0.5rem",
                            ),
                            padding="2rem",
                            border_radius="1rem",
                            border="1px solid",
                            border_color="gray.200",
                            _hover={"box_shadow": "0 8px 16px rgba(0, 0, 0, 0.1)"},
                        ),
                        rx.box(
                            rx.icon(tag="zap", size=40, color="#76B900"),
                            rx.heading("Latency Reduction", font_size="1.3rem", margin_top="1rem"),
                            rx.text(
                                "Optimize model architecture and computation graphs to reduce inference latency",
                                color="gray.600",
                                margin_top="0.5rem",
                            ),
                            padding="2rem",
                            border_radius="1rem",
                            border="1px solid",
                            border_color="gray.200",
                            _hover={"box_shadow": "0 8px 16px rgba(0, 0, 0, 0.1)"},
                        ),
                        rx.box(
                            rx.icon(tag="cpu", size=40, color="#76B900"),
                            rx.heading("Resource Utilization", font_size="1.3rem", margin_top="1rem"),
                            rx.text(
                                "Intelligent scheduling algorithms to maximize GPU/CPU utilization",
                                color="gray.600",
                                margin_top="0.5rem",
                            ),
                            padding="2rem",
                            border_radius="1rem",
                            border="1px solid",
                            border_color="gray.200",
                            _hover={"box_shadow": "0 8px 16px rgba(0, 0, 0, 0.1)"},
                        ),
                        rx.box(
                            rx.icon(tag="trending-up", size=40, color="#76B900"),
                            rx.heading("Memory Optimization", font_size="1.3rem", margin_top="1rem"),
                            rx.text(
                                "Reduce memory footprint to support larger-scale model deployments",
                                color="gray.600",
                                margin_top="0.5rem",
                            ),
                            padding="2rem",
                            border_radius="1rem",
                            border="1px solid",
                            border_color="gray.200",
                            _hover={"box_shadow": "0 8px 16px rgba(0, 0, 0, 0.1)"},
                        ),
                        columns="2",
                        spacing="4",
                        margin_top="1rem",
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
