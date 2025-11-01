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


def model_table_row(model_dict: dict) -> rx.Component:
    """Create a table row for a model with name and HuggingFace URL."""
    return rx.table.row(
        # Model Name cell
        rx.table.cell(
            rx.hstack(
                rx.box(
                    rx.icon(tag="box", size=18, color="#76B900"),
                    padding="0.4rem",
                    border_radius="0.4rem",
                    background="linear-gradient(135deg, rgba(118, 185, 0, 0.1) 0%, rgba(118, 185, 0, 0.05) 100%)",
                ),
                rx.text(
                    model_dict["model_name"],
                    font_weight="600",
                    font_size="0.9rem",
                    color="#2d3748",
                ),
                spacing="2",
                align="center",
            ),
        ),
        # HuggingFace URL cell - only show icon
        rx.table.cell(
            rx.link(
                rx.icon(
                    tag="external_link",
                    size=20,
                    color="#3B82F6",
                    _hover={"color": "#2563EB", "transform": "scale(1.1)"},
                ),
                href=model_dict["huggingface_url"],
                is_external=True,
            ),
            text_align="center",
        ),
        # Actions cell (only in edit mode)
        rx.cond(
            State.is_editing_models,
            rx.table.cell(
                rx.hstack(
                    # Move buttons group
                    rx.hstack(
                        # Move up button
                        rx.button(
                            rx.icon(tag="chevron_up", size=16),
                            on_click=lambda: State.move_model_up_by_name(model_dict["model_name"]),
                            size="1",
                            variant="ghost",
                            color_scheme="blue",
                            _hover={
                                "background": "rgba(59, 130, 246, 0.1)",
                            },
                        ),
                        # Move down button
                        rx.button(
                            rx.icon(tag="chevron_down", size=16),
                            on_click=lambda: State.move_model_down_by_name(model_dict["model_name"]),
                            size="1",
                            variant="ghost",
                            color_scheme="blue",
                            _hover={
                                "background": "rgba(59, 130, 246, 0.1)",
                            },
                        ),
                        spacing="1",
                        padding="0.2rem",
                        border_radius="0.4rem",
                        background="rgba(59, 130, 246, 0.05)",
                    ),
                    # Delete button (separated)
                    rx.button(
                        rx.icon(tag="trash_2", size=16),
                        on_click=lambda: State.open_delete_confirm(model_dict["model_name"]),
                        size="1",
                        variant="ghost",
                        color_scheme="red",
                        _hover={
                            "background": "rgba(239, 68, 68, 0.1)",
                        },
                    ),
                    spacing="2",
                    justify="end",
                ),
                text_align="right",
            ),
            rx.fragment(),  # Empty fragment when not editing
        ),
        _hover={
            "background": "linear-gradient(135deg, rgba(118, 185, 0, 0.03) 0%, rgba(255, 255, 255, 1) 100%)",
        },
    )


def quantization_page() -> rx.Component:
    """Quantization page."""
    return rx.fragment(
        # Delete Confirmation Dialog
        rx.dialog.root(
            rx.dialog.content(
                rx.dialog.title("Confirm Deletion"),
                rx.dialog.description(
                    f"Are you sure to delete '{State.model_to_delete}'?.",
                    margin_bottom="1rem",
                ),
                rx.hstack(
                    rx.dialog.close(
                        rx.button(
                            "Cancel",
                            size="3",
                            variant="soft",
                            color_scheme="gray",
                            on_click=State.close_delete_confirm,
                        ),
                    ),
                    rx.button(
                        "Delete",
                        size="3",
                        color_scheme="red",
                        on_click=State.confirm_delete_model,
                    ),
                    spacing="3",
                    justify="end",
                ),
            ),
            open=State.show_delete_confirm,
        ),
        # Main Content
        rx.hstack(
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
                                    rx.icon(tag="microchip", size=18, color="#EC4899"),
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
                                            rx.icon(tag="pencil", size=18),
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
                                    ["Ampere", "Ada", "Hopper", "Blackwell"],
                                    value=State.selected_architecture.capitalize(),
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
                                                placeholder="Enter HuggingFace URL (e.g., https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct)",
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
                                    rx.hstack(
                                        rx.icon(tag="list", size=20, color="#3B82F6"),
                                        rx.text(
                                            "Current Models",
                                            font_weight="600",
                                            font_size="1rem",
                                        ),
                                        spacing="2",
                                        align="center",
                                        margin_bottom="0.75rem",
                                    ),
                                    rx.cond(
                                        State.current_architecture_models.length() > 0,
                                        rx.table.root(
                                            rx.table.header(
                                                rx.table.row(
                                                    rx.table.column_header_cell("Model Name", width=rx.cond(State.is_editing_models, "60%", "75%")),
                                                    rx.table.column_header_cell("Link", width=rx.cond(State.is_editing_models, "15%", "25%"), text_align="center"),
                                                    rx.cond(
                                                        State.is_editing_models,
                                                        rx.table.column_header_cell("Actions", width="25%", text_align="right"),
                                                        rx.fragment(),
                                                    ),
                                                ),
                                            ),
                                            rx.table.body(
                                                rx.foreach(
                                                    State.current_architecture_models,
                                                    model_table_row,
                                                ),
                                            ),
                                            variant="surface",
                                            size="2",
                                            width="100%",
                                        ),
                                        rx.box(
                                            rx.vstack(
                                                rx.icon(tag="inbox", size=48, color="gray.300"),
                                                rx.text(
                                                    "No models found",
                                                    font_weight="500",
                                                    color="gray.600",
                                                ),
                                                rx.text(
                                                    "Click 'Edit' and add a model to get started",
                                                    font_size="0.85rem",
                                                    color="gray.500",
                                                ),
                                                spacing="2",
                                                align="center",
                                            ),
                                            padding="2rem",
                                            width="100%",
                                        ),
                                    ),
                                    spacing="2",
                                    width="100%",
                                ),
                                padding="1.25rem",
                                border_radius="0.75rem",
                                background="linear-gradient(135deg, rgba(59, 130, 246, 0.03) 0%, rgba(255, 255, 255, 1) 100%)",
                                border="1px solid rgba(59, 130, 246, 0.15)",
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
                    on_mount=[State.load_ampere_data, State.reset_edit_mode],
                ),
                max_width="1200px",
            ),
            margin_left="250px",
            width="100%",
        ),
        spacing="0",
        align="start",
        ),
    )
