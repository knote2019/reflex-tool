"""Ada Architecture Performance page."""
import reflex as rx
from ..components.navbar import navbar
from .. import State


def model_performance_chart(model: str) -> rx.Component:
    """Create a performance chart for a specific model."""
    return rx.box(
        rx.vstack(
            rx.heading(
                model,
                font_size="1rem",
                font_weight="600",
                margin_bottom="0.5rem",
            ),
            rx.recharts.bar_chart(
                rx.recharts.bar(
                    data_key="throughput",
                    fill="#3B82F6",
                    radius=[8, 8, 0, 0],
                ),
                rx.recharts.x_axis(data_key="format"),
                rx.recharts.y_axis(
                    label={"value": "Tokens/sec", "angle": -90, "position": "insideLeft"}
                ),
                rx.recharts.cartesian_grid(stroke_dasharray="3 3"),
                rx.recharts.graphing_tooltip(),
                data=State.get_ada_performance_chart_data(model),
                width="100%",
                height=250,
            ),
            spacing="2",
            width="100%",
        ),
        padding="1rem",
        border_radius="0.5rem",
        background="rgba(59, 130, 246, 0.02)",
        border="1px solid rgba(59, 130, 246, 0.1)",
        margin_bottom="1rem",
        width="100%",
    )


def performance_ada_page() -> rx.Component:
    """Ada Architecture Performance page."""
    return rx.hstack(
        navbar(),
        rx.box(
            rx.container(
                rx.vstack(
                    # Title
                    rx.heading(
                        "Ada Architecture - Performance Optimization",
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
                                "Ada GPUs",
                                font_size="1.2rem",
                                color="#3B82F6",
                                margin_bottom="0.5rem",
                            ),
                            rx.hstack(
                                rx.badge("RTX 4090", color_scheme="blue", variant="soft", size="2"),
                                rx.badge("RTX 6000 Ada", color_scheme="blue", variant="soft", size="2"),
                                spacing="2",
                                wrap="wrap",
                            ),
                        ),
                        padding="1rem",
                        border_radius="0.5rem",
                        background="rgba(59, 130, 246, 0.05)",
                        border="1px solid rgba(59, 130, 246, 0.2)",
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
                            on_change=State.set_modelopt_version_and_reload_ada_performance,
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
                                "L40s",
                            ],
                            placeholder="Select GPU",
                            value=State.selected_gpu_name,
                            on_change=State.set_gpu_name_and_reload_ada_performance,
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
                                rx.icon(tag="activity", size=32, color="#3B82F6"),
                                rx.heading(
                                    "Model Performance - Token Throughput",
                                    font_size="1.3rem",
                                ),
                                rx.spacer(),
                                rx.button(
                                    rx.icon(tag="refresh_cw", size=18),
                                    "refresh",
                                    on_click=State.refresh_ada_performance_data,
                                    variant="outline",
                                    size="2",
                                    color_scheme="blue",
                                ),
                                spacing="2",
                                align="center",
                                margin_bottom="1.5rem",
                                width="100%",
                            ),
                            # Charts for each model
                            rx.foreach(
                                State.ada_test_models,
                                model_performance_chart,
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
                    on_mount=State.load_ada_performance_data,
                ),
                max_width="1200px",
            ),
            margin_left="250px",
            width="100%",
        ),
        spacing="0",
        align="start",
    )

