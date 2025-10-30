"""Application state."""
import reflex as rx


class State(rx.State):
    """Application state."""
    selected_modelopt_version: str = "0.39.0"
    selected_gpu: str = "H200"
    selected_model: str = "Llama-3.1-8B-Instruct"
    selected_quantization: str = "fp8"
    
    # Test status: "passed", "failed", "unsupported"
    # For demonstration, we'll set different statuses for different combinations
    test_status: dict[str, str] = {
        # Llama-3.1-8B-Instruct - all passed
        "Llama-3.1-8B-Instruct_fp8": "passed",
        "Llama-3.1-8B-Instruct_int8_sq": "passed",
        "Llama-3.1-8B-Instruct_int4_awq": "passed",
        "Llama-3.1-8B-Instruct_w4a8_awq": "passed",
        "Llama-3.1-8B-Instruct_nvfp4": "passed",
        # Llama-3.3-70B-Instruct - some failed
        "Llama-3.3-70B-Instruct_fp8": "passed",
        "Llama-3.3-70B-Instruct_int8_sq": "passed",
        "Llama-3.3-70B-Instruct_int4_awq": "failed",
        "Llama-3.3-70B-Instruct_w4a8_awq": "passed",
        "Llama-3.3-70B-Instruct_nvfp4": "unsupported",
        # Llama-4-Scout-17B-16E-Instruct
        "Llama-4-Scout-17B-16E-Instruct_fp8": "passed",
        "Llama-4-Scout-17B-16E-Instruct_int8_sq": "passed",
        "Llama-4-Scout-17B-16E-Instruct_int4_awq": "passed",
        "Llama-4-Scout-17B-16E-Instruct_w4a8_awq": "failed",
        "Llama-4-Scout-17B-16E-Instruct_nvfp4": "passed",
        # Default all others to passed for now
    }

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

    def get_test_status(self, model: str, quantization_format: str) -> str:
        """Get test status for specific model and quantization format."""
        key = f"{model}_{quantization_format}"
        return self.test_status.get(key, "passed")  # Default to passed

    def download_log(self, model: str, quantization_format: str):
        """Download log for specific model and quantization format."""
        status = self.get_test_status(model, quantization_format)
        # Generate log content
        log_content = f"""Quantization Log
=================
Model: {model}
Quantization Format: {quantization_format}
ModelOpt Version: {self.selected_modelopt_version}
GPU: {self.selected_gpu}
Test Status: {status.upper()}
Timestamp: 2025-01-15 10:30:00

Status: Completed
"""
        # Create download filename
        filename = f"{model}_{quantization_format}.log"
        return rx.download(data=log_content, filename=filename)
