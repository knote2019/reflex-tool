"""Contact page."""
import reflex as rx
from ..components.navbar import navbar


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
                            rx.icon(tag="mail", size=24, color="#76B900"),
                            rx.text("Email: tech@nvidia.com", font_size="1rem"),
                            spacing="2",
                            align="center",
                        ),
                        rx.hstack(
                            rx.icon(tag="phone", size=24, color="#76B900"),
                            rx.text("Phone: +1 (408) 486-2000", font_size="1rem"),
                            spacing="2",
                            align="center",
                        ),
                        rx.hstack(
                            rx.icon(tag="github", size=24, color="#76B900"),
                            rx.text("GitHub: github.com/NVIDIA", font_size="1rem"),
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
