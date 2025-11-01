"""Ada Architecture Performance page."""
import reflex as rx
from ..components.navbar import navbar
from .. import State


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
                                rx.badge("L40s", color_scheme="blue", variant="soft", size="2"),
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
                    # Model Name, Quantization Format and GPU selection
                    rx.hstack(
                        rx.text(
                            "Model Name:",
                            font_weight="500",
                            font_size="0.95rem",
                        ),
                        rx.select(
                            State.ada_test_models,
                            placeholder="All Models",
                            value=State.selected_performance_model,
                            on_change=State.set_selected_performance_model,
                            size="2",
                            width="300px",
                        ),
                        rx.text(
                            "Quantization Format:",
                            font_weight="500",
                            font_size="0.95rem",
                            margin_left="0.5rem",
                        ),
                        rx.select(
                            State.ada_quantization_formats,
                            placeholder="All Formats",
                            value=State.selected_performance_format,
                            on_change=State.set_selected_performance_format,
                            size="2",
                            width="150px",
                        ),
                        rx.text(
                            "GPU Name:",
                            font_weight="500",
                            font_size="0.95rem",
                            margin_left="0.5rem",
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
                        wrap="wrap",
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
                            # Grouped bar chart showing throughput and latency across versions
                            rx.recharts.bar_chart(
                                rx.recharts.bar(
                                    data_key="throughput",
                                    fill="#3B82F6",
                                    name="Token Throughput (tokens/sec)",
                                    radius=[4, 4, 0, 0],
                                ),
                                rx.recharts.bar(
                                    data_key="latency",
                                    fill="#FFB900",
                                    name="Total Latency (ms)",
                                    radius=[4, 4, 0, 0],
                                ),
                                rx.recharts.x_axis(
                                    data_key="version",
                                    label={"value": "TensorRT-LLM Version", "position": "insideBottom", "offset": -5}
                                ),
                                rx.recharts.y_axis(
                                    label={"value": "Performance Metrics", "angle": -90, "position": "insideLeft"}
                                ),
                                rx.recharts.cartesian_grid(stroke_dasharray="3 3"),
                                rx.recharts.graphing_tooltip(
                                    cursor={"fill": "rgba(59, 130, 246, 0.1)"},
                                    content_style={
                                        "backgroundColor": "white",
                                        "border": "1px solid #ccc",
                                        "borderRadius": "4px",
                                        "padding": "8px"
                                    }
                                ),
                                rx.recharts.legend(),
                                data=State.ada_performance_chart_data,
                                width="100%",
                                height=400,
                                margin={"top": 20, "right": 30, "left": 20, "bottom": 40},
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

