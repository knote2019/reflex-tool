"""Contact page."""
import reflex as rx
from ..components.navbar import navbar


def contact_page() -> rx.Component:
    """Contact page."""
    return rx.hstack(
        navbar(),
        rx.box(
            rx.container(
                rx.vstack(
                    rx.heading(
                        "Contact Us",
                        font_size="1.8rem",
                        font_weight="600",
                        margin_top="1.5rem",
                        margin_bottom="1rem",
                    ),
                    rx.box(
                        rx.vstack(
                            rx.hstack(
                                rx.icon(tag="mail", size=24, color="#76B900"),
                                rx.text("Email: minghongk@nvidia.com", font_size="1rem"),
                                spacing="2",
                                align="center",
                            ),
                            spacing="4",
                            align="start",
                        ),
                        padding="3rem",
                        border_radius="1rem",
                        box_shadow="0 4px 6px rgba(0, 0, 0, 0.1)",
                        background="white",
                        margin_top="1rem",
                    ),
                    spacing="4",
                    padding="2rem",
                    align="start",
                ),
                max_width="1200px",
            ),
            margin_left="250px",
            width="100%",
        ),
        spacing="0",
        align="start",
    )
