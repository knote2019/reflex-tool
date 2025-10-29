"""Application state."""
import reflex as rx


class State(rx.State):
    """Application state."""
    selected_model: str = "Llama-3.1-8B-Instruct"
    
    def set_model(self, model: str):
        """Set the selected model."""
        self.selected_model = model

