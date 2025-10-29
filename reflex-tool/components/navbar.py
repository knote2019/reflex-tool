"""Navigation bar component."""
import reflex as rx


def navbar() -> rx.Component:
    """Create navigation bar component."""
    return rx.box(
        rx.hstack(
            # Logo and brand name
            rx.hstack(
                rx.icon(
                    tag="cpu",
                    size=32,
                    color="#76B900",
                ),
                rx.text(
                    "NVIDIA Model Optimizer",
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
        background="linear-gradient(135deg, #76B900 0%, #5A8C00 100%)",
        padding="1rem 2rem",
        box_shadow="0 4px 6px rgba(0, 0, 0, 0.1)",
        position="sticky",
        top="0",
        z_index="1000",
        width="100%",
    )
