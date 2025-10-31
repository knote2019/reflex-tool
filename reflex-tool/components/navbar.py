"""Navigation bar component."""
import reflex as rx


def nav_link(text: str, icon: str, href: str, is_home: bool = False) -> rx.Component:
    """Create a navigation link with active state highlighting."""
    # For home page, match exact path. For others, check if current path starts with href
    is_active = rx.cond(
        is_home,
        rx.State.router.page.path == "/",
        rx.State.router.page.path.startswith(href),
    )
    
    return rx.link(
        rx.hstack(
            rx.icon(tag=icon, size=20),
            rx.text(text),
            spacing="3",
            align="center",
        ),
        href=href,
        color="white",
        padding="0.75rem 1rem",
        border_radius="0.5rem",
        width="100%",
        background=rx.cond(
            is_active,
            "rgba(255, 255, 255, 0.25)",
            "transparent",
        ),
        font_weight=rx.cond(
            is_active,
            "600",
            "normal",
        ),
        _hover={
            "background_color": "rgba(255, 255, 255, 0.15)",
            "text_decoration": "none",
        },
    )


def navbar() -> rx.Component:
    """Create navigation sidebar component."""
    return rx.box(
        rx.vstack(
            # Logo and brand name at top
            rx.vstack(
                rx.icon(
                    tag="cpu",
                    size=48,
                    color="#76B900",
                ),
                rx.text(
                    "NVIDIA",
                    font_size="1.3rem",
                    font_weight="bold",
                    color="white",
                    text_align="center",
                ),
                rx.text(
                    "Model Optimizer",
                    font_size="0.9rem",
                    color="rgba(255, 255, 255, 0.8)",
                    text_align="center",
                ),
                spacing="2",
                align="center",
                padding_bottom="2rem",
                border_bottom="1px solid rgba(255, 255, 255, 0.2)",
                width="100%",
            ),
            # Navigation links
            rx.vstack(
                nav_link("Home", "home", "/", is_home=True),
                nav_link("Quantization", "layers", "/quantization"),
                nav_link("Inference", "zap", "/inference"),
                nav_link("Performance", "activity", "/performance"),
                nav_link("Contact", "mail", "/contact"),
                spacing="2",
                width="100%",
                padding_top="2rem",
            ),
            # Bottom button
            rx.box(
                rx.button(
                    rx.hstack(
                        rx.icon(tag="log_in", size=20),
                        rx.text("Login"),
                        spacing="2",
                    ),
                    variant="outline",
                    size="3",
                    color="white",
                    border_color="white",
                    width="100%",
                    _hover={
                        "background_color": "rgba(255, 255, 255, 0.2)",
                    },
                ),
                margin_top="auto",
                width="100%",
            ),
            spacing="0",
            align="start",
            height="100%",
            padding="2rem 1rem",
        ),
        background="linear-gradient(180deg, #76B900 0%, #5A8C00 100%)",
        box_shadow="4px 0 6px rgba(0, 0, 0, 0.1)",
        position="fixed",
        left="0",
        top="0",
        height="100vh",
        width="250px",
        z_index="1000",
    )
