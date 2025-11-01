"""Ampere Architecture Performance page."""
import reflex as rx
from ..components.navbar import navbar
from .. import State


def performance_ampere_page() -> rx.Component:
    """Ampere Architecture Performance page."""
    return rx.hstack(
        navbar(),
        rx.box(
            rx.container(
                rx.vstack(
                    # Title
                    rx.heading(
                        "Ampere Architecture - Performance Optimization",
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
                        href="/performance",
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
                    # Model Name and GPU selection
                    rx.hstack(
                        rx.text(
                            "Model Name:",
                            font_weight="500",
                            font_size="0.95rem",
                        ),
                        rx.select(
                            State.ampere_test_models,
                            placeholder="Select model",
                            value=State.selected_performance_model,
                            on_change=State.set_selected_performance_model,
                            size="2",
                            width="300px",
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
                            placeholder="Select GPU",
                            value=State.selected_gpu_name,
                            on_change=State.set_gpu_name_and_reload_ampere_performance,
                            size="2",
                            width="150px",
                        ),
                        spacing="3",
                        align="center",
                        margin_bottom="0.5rem",
                    ),
                    # Model & Quantization Format chart
                    rx.box(
                        rx.vstack(
                            rx.hstack(
                                rx.icon(tag="activity", size=32, color="#76B900"),
                                rx.heading(
                                    "Model Performance - Token Throughput",
                                    font_size="1.3rem",
                                ),
                                rx.spacer(),
                                rx.button(
                                    rx.icon(tag="refresh_cw", size=18),
                                    "refresh",
                                    on_click=State.refresh_ampere_performance_data,
                                    variant="outline",
                                    size="2",
                                    color_scheme="green",
                                ),
                                spacing="2",
                                align="center",
                                margin_bottom="1.5rem",
                                width="100%",
                            ),
                            # Grouped bar chart for selected model(s)
                            rx.recharts.bar_chart(
                                rx.cond(
                                    State.selected_performance_model != "",
                                    # Single model selected
                                    rx.recharts.bar(
                                        data_key=State.selected_performance_model,
                                        fill="#76B900",
                                        name=State.selected_performance_model,
                                        radius=[8, 8, 0, 0],
                                    ),
                                    # All models
                                    rx.foreach(
                                        State.ampere_test_models,
                                        lambda model: rx.recharts.bar(
                                            data_key=model,
                                            fill="#76B900",
                                            name=model,
                                            radius=[4, 4, 0, 0],
                                        ),
                                    ),
                                ),
                                rx.recharts.x_axis(data_key="format"),
                                rx.recharts.y_axis(
                                    label={"value": "Tokens/sec", "angle": -90, "position": "insideLeft"}
                                ),
                                rx.recharts.cartesian_grid(stroke_dasharray="3 3"),
                                rx.recharts.graphing_tooltip(),
                                rx.recharts.legend(),
                                data=State.ampere_performance_chart_data,
                                width="100%",
                                height=400,
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
                        max_width="1000px",
                    ),
                    spacing="4",
                    padding="2rem",
                    on_mount=State.load_ampere_performance_data,
                ),
                max_width="1200px",
            ),
            margin_left="250px",
            width="100%",
        ),
        spacing="0",
        align="start",
    )

