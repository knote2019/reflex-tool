"""Home page."""
import reflex as rx
from ..components.navbar import navbar


def home_page() -> rx.Component:
    """Home page."""
    return rx.box(
        navbar(),
        rx.container(
            rx.vstack(
                rx.heading(
                    "Welcome to NVIDIA Model Optimizer",
                    font_size="3rem",
                    margin_top="4rem",
                    text_align="center",
                ),
                rx.text(
                    "Advanced AI model optimization platform for efficient deployment",
                    font_size="1.3rem",
                    color="gray.600",
                    text_align="center",
                    margin_top="1rem",
                ),
                rx.text(
                    "Accelerate your deep learning models with cutting-edge optimization techniques",
                    font_size="1.1rem",
                    color="gray.500",
                    text_align="center",
                    margin_top="0.5rem",
                ),
                # Feature highlights
                rx.grid(
                    rx.box(
                        rx.icon(tag="zap", size=48, color="#76B900"),
                        rx.heading("Fast Performance", font_size="1.5rem", margin_top="1rem"),
                        rx.text(
                            "Optimize your models for maximum speed and efficiency",
                            color="gray.600",
                            text_align="center",
                            margin_top="0.5rem",
                        ),
                        padding="2rem",
                        border_radius="1rem",
                        box_shadow="0 4px 6px rgba(0, 0, 0, 0.1)",
                        _hover={"box_shadow": "0 8px 12px rgba(0, 0, 0, 0.15)"},
                    ),
                    rx.box(
                        rx.icon(tag="shield", size=48, color="#76B900"),
                        rx.heading("Enterprise Ready", font_size="1.5rem", margin_top="1rem"),
                        rx.text(
                            "Production-grade tools trusted by leading organizations",
                            color="gray.600",
                            text_align="center",
                            margin_top="0.5rem",
                        ),
                        padding="2rem",
                        border_radius="1rem",
                        box_shadow="0 4px 6px rgba(0, 0, 0, 0.1)",
                        _hover={"box_shadow": "0 8px 12px rgba(0, 0, 0, 0.15)"},
                    ),
                    rx.box(
                        rx.icon(tag="code", size=48, color="#76B900"),
                        rx.heading("Easy Integration", font_size="1.5rem", margin_top="1rem"),
                        rx.text(
                            "Seamlessly integrate with your existing ML workflows",
                            color="gray.600",
                            text_align="center",
                            margin_top="0.5rem",
                        ),
                        padding="2rem",
                        border_radius="1rem",
                        box_shadow="0 4px 6px rgba(0, 0, 0, 0.1)",
                        _hover={"box_shadow": "0 8px 12px rgba(0, 0, 0, 0.15)"},
                    ),
                    columns="3",
                    spacing="4",
                    margin_top="4rem",
                ),
                # Call to action
                rx.hstack(
                    rx.button(
                        "Get Started",
                        size="4",
                        background="linear-gradient(135deg, #76B900 0%, #5A8C00 100%)",
                        color="white",
                        padding="1.5rem 3rem",
                        font_size="1.2rem",
                        _hover={"opacity": "0.9"},
                        on_click=rx.redirect("/quantization"),
                    ),
                    rx.button(
                        "Learn More",
                        size="4",
                        variant="outline",
                        color="#76B900",
                        border_color="#76B900",
                        padding="1.5rem 3rem",
                        font_size="1.2rem",
                        _hover={"background_color": "rgba(118, 185, 0, 0.1)"},
                        on_click=rx.redirect("/performance"),
                    ),
                    spacing="4",
                    margin_top="3rem",
                    justify="center",
                ),
                spacing="4",
                padding="2rem",
            ),
            max_width="1200px",
        ),
    )

