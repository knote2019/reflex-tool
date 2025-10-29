"""Performance page."""
import reflex as rx
from ..components.navbar import navbar


def performance_page() -> rx.Component:
    """Performance page."""
    return rx.box(
        navbar(),
        rx.container(
            rx.vstack(
                rx.heading(
                    "Performance Optimization",
                    font_size="2.5rem",
                    margin_top="3rem",
                ),
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
                    margin_top="2rem",
                ),
                spacing="4",
                padding="2rem",
            ),
            max_width="1000px",
        ),
    )
