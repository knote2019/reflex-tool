"""Main application file - contains navbar and pages."""
import reflex as rx


class State(rx.State):
    """Application state."""
    pass


def navbar() -> rx.Component:
    """Create navigation bar component."""
    return rx.box(
        rx.hstack(
            # Logo and brand name
            rx.hstack(
                rx.icon(
                    tag="layout-dashboard",
                    size=32,
                    color="white",
                ),
                rx.text(
                    "Model Optimizer",
                    font_size="1.5rem",
                    font_weight="bold",
                    color="white",
                ),
                spacing="2",
            ),
            # Navigation links
            rx.hstack(
                rx.link(
                    "Quantization",
                    href="/",
                    color="white",
                    padding="0.5rem 1rem",
                    border_radius="0.5rem",
                    _hover={
                        "background_color": "rgba(255, 255, 255, 0.1)",
                        "text_decoration": "none",
                    },
                ),
                rx.link(
                    "Inference",
                    href="/inference",
                    color="white",
                    padding="0.5rem 1rem",
                    border_radius="0.5rem",
                    _hover={
                        "background_color": "rgba(255, 255, 255, 0.1)",
                        "text_decoration": "none",
                    },
                ),
                rx.link(
                    "Performance",
                    href="/performance",
                    color="white",
                    padding="0.5rem 1rem",
                    border_radius="0.5rem",
                    _hover={
                        "background_color": "rgba(255, 255, 255, 0.1)",
                        "text_decoration": "none",
                    },
                ),
                rx.link(
                    "Contact",
                    href="/contact",
                    color="white",
                    padding="0.5rem 1rem",
                    border_radius="0.5rem",
                    _hover={
                        "background_color": "rgba(255, 255, 255, 0.1)",
                        "text_decoration": "none",
                    },
                ),
                spacing="1",
            ),
            # Right side button
            rx.button(
                "Login",
                variant="outline",
                size="3",
                color="white",
                border_color="white",
                _hover={
                    "background_color": "rgba(255, 255, 255, 0.2)",
                },
            ),
            justify="between",
            align="center",
            width="100%",
        ),
        background="linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
        padding="1rem 2rem",
        box_shadow="0 4px 6px rgba(0, 0, 0, 0.1)",
        position="sticky",
        top="0",
        z_index="1000",
        width="100%",
    )


def quantization_page() -> rx.Component:
    """Quantization page."""
    return rx.box(
        navbar(),
        rx.container(
            rx.vstack(
                rx.heading(
                    "Model Quantization",
                    font_size="3rem",
                    margin_top="4rem",
                    text_align="center",
                ),
                rx.text(
                    "Efficient model quantization techniques to reduce model size and improve inference speed",
                    font_size="1.2rem",
                    color="gray.600",
                    text_align="center",
                    margin_top="1rem",
                ),
                rx.hstack(
                    rx.box(
                        rx.icon(tag="zap", size=48, color="#667eea"),
                        rx.heading("INT8 Quantization", font_size="1.5rem", margin_top="1rem"),
                        rx.text(
                            "Reduce model precision to 8-bit integers, significantly reducing model size",
                            color="gray.600",
                            text_align="center",
                        ),
                        padding="2rem",
                        border_radius="1rem",
                        box_shadow="0 4px 6px rgba(0, 0, 0, 0.1)",
                        width="300px",
                    ),
                    rx.box(
                        rx.icon(tag="layers", size=48, color="#667eea"),
                        rx.heading("Dynamic Quantization", font_size="1.5rem", margin_top="1rem"),
                        rx.text(
                            "Runtime dynamic quantization, balancing accuracy and performance",
                            color="gray.600",
                            text_align="center",
                        ),
                        padding="2rem",
                        border_radius="1rem",
                        box_shadow="0 4px 6px rgba(0, 0, 0, 0.1)",
                        width="300px",
                    ),
                    rx.box(
                        rx.icon(tag="sparkles", size=48, color="#667eea"),
                        rx.heading("Mixed Precision", font_size="1.5rem", margin_top="1rem"),
                        rx.text(
                            "Use different precision for different layers to optimize performance",
                            color="gray.600",
                            text_align="center",
                        ),
                        padding="2rem",
                        border_radius="1rem",
                        box_shadow="0 4px 6px rgba(0, 0, 0, 0.1)",
                        width="300px",
                    ),
                    spacing="4",
                    margin_top="3rem",
                    wrap="wrap",
                    justify="center",
                ),
                spacing="4",
                padding="2rem",
            ),
            max_width="1200px",
        ),
    )


def inference_page() -> rx.Component:
    """Inference page."""
    return rx.box(
        navbar(),
        rx.container(
            rx.vstack(
                rx.heading(
                    "Model Inference",
                    font_size="2.5rem",
                    margin_top="3rem",
                ),
                rx.text(
                    "Efficient model inference engine supporting multiple deep learning frameworks, providing fast and stable inference services.",
                    font_size="1.1rem",
                    color="gray.700",
                    margin_top="1.5rem",
                    line_height="1.8",
                ),
                rx.text(
                    "Inference Engine Features:",
                    font_size="1.1rem",
                    font_weight="bold",
                    margin_top="2rem",
                ),
                rx.unordered_list(
                    rx.list_item("Support for multiple frameworks: PyTorch, TensorFlow, ONNX"),
                    rx.list_item("Batch processing optimization to improve throughput"),
                    rx.list_item("GPU/CPU hybrid scheduling for maximum resource utilization"),
                    rx.list_item("Low-latency inference with millisecond response times"),
                    font_size="1.1rem",
                    color="gray.700",
                    spacing="3",
                    margin_top="1rem",
                ),
                spacing="4",
                padding="2rem",
                align="start",
            ),
            max_width="800px",
        ),
    )


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
                        rx.icon(tag="activity", size=40, color="#667eea"),
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
                        rx.icon(tag="zap", size=40, color="#667eea"),
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
                        rx.icon(tag="cpu", size=40, color="#667eea"),
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
                        rx.icon(tag="trending-up", size=40, color="#667eea"),
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


def contact_page() -> rx.Component:
    """Contact page."""
    return rx.box(
        navbar(),
        rx.container(
            rx.vstack(
                rx.heading(
                    "Contact Us",
                    font_size="2.5rem",
                    margin_top="3rem",
                ),
                rx.box(
                    rx.vstack(
                        rx.text(
                            "Interested in our model optimization services? Contact our technical team!",
                            font_size="1.1rem",
                            color="gray.700",
                            margin_bottom="2rem",
                        ),
                        rx.hstack(
                            rx.icon(tag="mail", size=24, color="#667eea"),
                            rx.text("Email: tech@modelopt.com", font_size="1rem"),
                            spacing="2",
                            align="center",
                        ),
                        rx.hstack(
                            rx.icon(tag="phone", size=24, color="#667eea"),
                            rx.text("Phone: +1 (555) 123-4567", font_size="1rem"),
                            spacing="2",
                            align="center",
                        ),
                        rx.hstack(
                            rx.icon(tag="github", size=24, color="#667eea"),
                            rx.text("GitHub: github.com/modelopt", font_size="1rem"),
                            spacing="2",
                            align="center",
                        ),
                        spacing="4",
                        align="start",
                    ),
                    padding="3rem",
                    border_radius="1rem",
                    box_shadow="0 4px 6px rgba(0, 0, 0, 0.1)",
                    margin_top="2rem",
                ),
                spacing="4",
                padding="2rem",
                align="start",
            ),
            max_width="800px",
        ),
    )


# Create app and add pages
app = rx.App()
app.add_page(quantization_page, route="/")
app.add_page(inference_page, route="/inference")
app.add_page(performance_page, route="/performance")
app.add_page(contact_page, route="/contact")
