"""Quantization page."""
import reflex as rx
from ..components.navbar import navbar
from .. import State


def status_icon(model: str, quantization_format: str) -> rx.Component:
    """Return the appropriate status icon based on test status."""
    status_key = f"{model}_{quantization_format}"

    # Get the status value, default to "passed" if not found
    status_value = State.test_status.get(status_key, "passed")

    return rx.match(
        status_value,
        ("passed", rx.icon(tag="circle_check", size=20, color="#76B900")),
        ("failed", rx.icon(tag="circle_alert", size=20, color="#FFB900")),
        ("unsupported", rx.icon(tag="circle_x", size=20, color="#999999")),
        rx.icon(tag="circle_check", size=20, color="#76B900"),  # default
    )


def download_cell(model: str, quantization_format: str) -> rx.Component:
    """Create a cell with status icon and download button."""
    return rx.table.cell(
        rx.hstack(
            # Status icon
            status_icon(model, quantization_format),
            # Download button
            rx.button(
                rx.icon(tag="download", size=18),
                on_click=lambda: State.download_log(model, quantization_format),
                background="transparent",
                border="none",
                cursor="pointer",
                _hover={"background": "#f0f0f0", "transform": "scale(1.1)"},
                padding="0.3rem",
                color="#666666",
            ),
            spacing="2",
            align="center",
            justify="center",
        ),
        text_align="center",
    )


def model_list_item(model_name: str) -> rx.Component:
    """Create a list item for a model with optional delete button."""
    return rx.hstack(
        rx.text(model_name, font_weight="500", font_size="0.95rem"),
        rx.spacer(),
        rx.cond(
            State.is_editing_models,
            rx.button(
                rx.icon(tag="trash_2", size=16),
                on_click=lambda: State.remove_model_from_architecture(model_name),
                size="1",
                variant="ghost",
                color_scheme="red",
                _hover={"background": "rgba(239, 68, 68, 0.1)"},
            ),
            rx.box(),  # Empty box when not editing
        ),
        padding="0.5rem 0.75rem",
        border_radius="0.375rem",
        background="white",
        border="1px solid",
        border_color="gray.200",
        width="100%",
        _hover={"background": "gray.50"},
    )


def quantization_page() -> rx.Component:
    """Quantization page."""
    return rx.hstack(
        navbar(),
        rx.box(
            rx.container(
                rx.vstack(
                    # Title section - top
                    rx.heading(
                        "Model Quantization",
                        font_size="1.8rem",
                        font_weight="600",
                        margin_top="1.5rem",
                        margin_bottom="1rem",
                    ),
                    # GPU Type Sub-navigation
                    rx.hstack(
                        rx.link(
                            rx.button(
                                rx.hstack(
                                    rx.icon(tag="microchip", size=18, color="#76B900"),
                                    rx.text("Ampere"),
                                    spacing="2",
                                ),
                                variant="soft",
                                size="2",
                                color_scheme="green",
                            ),
                            href="/quantization/ampere",
                        ),
                        rx.link(
                            rx.button(
                                rx.hstack(
                                    rx.icon(tag="microchip", size=18, color="#3B82F6"),
                                    rx.text("Ada"),
                                    spacing="2",
                                ),
                                variant="outline",
                                size="2",
                            ),
                            href="/quantization/ada",
                        ),
                        rx.link(
                            rx.button(
                                rx.hstack(
                                    rx.icon(tag="microchip", size=18, color="#A855F7"),
                                    rx.text("Hopper"),
                                    spacing="2",
                                ),
                                variant="outline",
                                size="2",
                            ),
                            href="/quantization/hopper",
                        ),
                        rx.link(
                            rx.button(
                                rx.hstack(
                                    rx.icon(tag="microchip", size=18, color="#F97316"),
                                    rx.text("Blackwell"),
                                    spacing="2",
                                ),
                                variant="outline",
                                size="2",
                            ),
                            href="/quantization/blackwell",
                        ),
                        spacing="3",
                        margin_bottom="1.5rem",
                        padding="0.75rem",
                        border_radius="0.5rem",
                        background="rgba(118, 185, 0, 0.05)",
                        width="100%",
                    ),
                    # Model Management Section
                    rx.box(
                        rx.vstack(
                            rx.hstack(
                                rx.icon(tag="settings", size=32, color="#76B900"),
                                rx.heading(
                                    "Model Management",
                                    font_size="1.3rem",
                                ),
                                rx.spacer(),
                                rx.button(
                                    rx.cond(
                                        State.is_editing_models,
                                        rx.hstack(
                                            rx.icon(tag="check", size=18),
                                            rx.text("Done"),
                                            spacing="2",
                                        ),
                                        rx.hstack(
                                            rx.icon(tag="edit", size=18),
                                            rx.text("Edit"),
                                            spacing="2",
                                        ),
                                    ),
                                    on_click=State.toggle_edit_mode,
                                    size="2",
                                    variant="outline",
                                    color_scheme=rx.cond(
                                        State.is_editing_models,
                                        "green",
                                        "blue",
                                    ),
                                ),
                                spacing="2",
                                align="center",
                                margin_bottom="1rem",
                                width="100%",
                            ),
                            # Architecture Selector
                            rx.hstack(
                                rx.text(
                                    "Architecture:",
                                    font_weight="500",
                                    font_size="0.95rem",
                                ),
                                rx.select(
                                    ["ampere", "ada", "hopper", "blackwell"],
                                    value=State.selected_architecture,
                                    on_change=State.set_selected_architecture,
                                    size="2",
                                    width="200px",
                                ),
                                spacing="3",
                                align="center",
                                margin_bottom="1rem",
                            ),
                            # Add New Model Section (only visible in edit mode)
                            rx.cond(
                                State.is_editing_models,
                                rx.box(
                                    rx.vstack(
                                        rx.text(
                                            "Add New Model",
                                            font_weight="600",
                                            font_size="0.95rem",
                                            margin_bottom="0.5rem",
                                        ),
                                        rx.hstack(
                                            rx.input(
                                                placeholder="Enter model name (e.g., Llama-3.1-8B-Instruct)",
                                                value=State.new_model_name,
                                                on_change=State.set_new_model_name,
                                                size="2",
                                                width="100%",
                                            ),
                                            rx.button(
                                                rx.hstack(
                                                    rx.icon(tag="plus", size=18),
                                                    rx.text("Add"),
                                                    spacing="2",
                                                ),
                                                on_click=State.add_model_to_architecture,
                                                size="2",
                                                color_scheme="green",
                                            ),
                                            spacing="2",
                                            width="100%",
                                        ),
                                        spacing="2",
                                        width="100%",
                                    ),
                                    padding="1rem",
                                    border_radius="0.5rem",
                                    background="rgba(118, 185, 0, 0.05)",
                                    border="1px solid rgba(118, 185, 0, 0.2)",
                                    margin_bottom="1rem",
                                    width="100%",
                                ),
                                rx.box(),  # Empty box when not editing
                            ),
                            # Current Models List
                            rx.box(
                                rx.vstack(
                                    rx.text(
                                        "Current Models",
                                        font_weight="600",
                                        font_size="0.95rem",
                                        margin_bottom="0.5rem",
                                    ),
                                    rx.cond(
                                        State.current_architecture_models.length() > 0,
                                        rx.vstack(
                                            rx.foreach(
                                                State.current_architecture_models,
                                                model_list_item,
                                            ),
                                            spacing="2",
                                            width="100%",
                                        ),
                                        rx.text(
                                            "No models found. Add a model above.",
                                            color="gray.500",
                                            font_style="italic",
                                        ),
                                    ),
                                    spacing="2",
                                    width="100%",
                                ),
                                padding="1rem",
                                border_radius="0.5rem",
                                background="rgba(59, 130, 246, 0.05)",
                                border="1px solid rgba(59, 130, 246, 0.2)",
                                width="100%",
                            ),
                            spacing="3",
                            width="100%",
                        ),
                        padding="1.5rem",
                        border_radius="1rem",
                        box_shadow="0 4px 6px rgba(0, 0, 0, 0.1)",
                        background="white",
                        margin_top="1rem",
                        width="100%",
                        max_width="800px",
                    ),
                    spacing="4",
                    padding="2rem",
                    on_mount=State.load_ampere_data,
                ),
                max_width="1200px",
            ),
            margin_left="250px",
            width="100%",
        ),
        spacing="0",
        align="start",
    )
