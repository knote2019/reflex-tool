"""Application state."""
import reflex as rx


class State(rx.State):
    """Application state."""
    selected_model: str = "Llama-3.1-8B-Instruct"
    selected_gpu: str = "H200"
    selected_quantization: str = "fp8"

    def set_gpu(self, gpu: str):
        """Set the selected GPU."""
        self.selected_gpu = gpu

    def set_model(self, model: str):
        """Set the selected model."""
        self.selected_model = model

    def set_quantization(self, quantization: str):
        """Set the selected quantization format."""
        self.selected_quantization = quantization
