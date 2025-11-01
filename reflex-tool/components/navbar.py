"""Navigation bar component."""
import reflex as rx


def nav_link(href: str, icon: str, text: str) -> rx.Component:
    """Create a navigation link with active state highlighting."""
    # Check if current path matches this link
    is_active = rx.State.router.page.path == href
    # For detail pages (e.g., /quantization/ampere), also highlight the parent
    is_parent_active = rx.cond(
        href != "/",
        rx.State.router.page.path.startswith(href + "/"),
        False
    )
    
    return rx.link(
        rx.hstack(
            rx.icon(
                tag=icon,
                size=20,
                color=rx.cond(
                    is_active | is_parent_active,
                    "#FFFFFF",
                    "rgba(255, 255, 255, 0.85)"
                )
            ),
            rx.text(
                text,
                color=rx.cond(
                    is_active | is_parent_active,
                    "#FFFFFF",
                    "rgba(255, 255, 255, 0.85)"
                )
            ),
            spacing="3",
            align="center",
        ),
        href=href,
        padding="0.75rem 1rem",
        border_radius="0.5rem",
        width="100%",
        background_color=rx.cond(
            is_active | is_parent_active,
            "rgba(255, 255, 255, 0.25)",
            "transparent"
        ),
        font_weight=rx.cond(
            is_active | is_parent_active,
            "600",
            "400"
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
                nav_link("/", "home", "Home"),
                nav_link("/quantization", "layers", "Quantization"),
                nav_link("/inference", "zap", "Inference"),
                nav_link("/performance", "activity", "Performance"),
                nav_link("/contact", "mail", "Contact"),
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
