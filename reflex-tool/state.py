"""Application state."""
import reflex as rx


class State(rx.State):
    """Application state."""
    selected_modelopt_version: str = "0.39.0"
    selected_gpu: str = "H200"
    selected_model: str = "Llama-3.1-8B-Instruct"
    selected_quantization: str = "fp8"

    def set_modelopt_version(self, version: str):
        """Set the selected ModelOpt version."""
        self.selected_modelopt_version = version

    def set_gpu(self, gpu: str):
        """Set the selected GPU."""
        self.selected_gpu = gpu

    def set_model(self, model: str):
        """Set the selected model."""
        self.selected_model = model

    def set_quantization(self, quantization: str):
        """Set the selected quantization format."""
        self.selected_quantization = quantization

    def download_log(self, model: str, quantization_format: str):
        """Download log for specific model and quantization format."""
        # Generate log content
        log_content = f"""Quantization Log
=================
Model: {model}
Quantization Format: {quantization_format}
ModelOpt Version: {self.selected_modelopt_version}
GPU: {self.selected_gpu}
Timestamp: 2025-01-15 10:30:00

Status: Completed Successfully
"""
        # Create download filename
        filename = f"{model}_{quantization_format}.log"
        return rx.download(data=log_content, filename=filename)
