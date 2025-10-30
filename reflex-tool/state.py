"""Application state."""
import reflex as rx
import csv
import os
from pathlib import Path


class State(rx.State):
    """Application state."""
    selected_modelopt_version: str = "0.39.0"
    selected_gpu: str = "H200"
    selected_model: str = "Llama-3.1-8B-Instruct"
    selected_quantization: str = "fp8"
    
    # Ampere test results data
    ampere_test_data: list[dict] = []
    
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

    def load_ampere_data(self):
        """Load Ampere test results from CSV file."""
        csv_path = Path(__file__).parent / "data" / "ampere_test_results.csv"
        
        if not csv_path.exists():
            print(f"CSV file not found: {csv_path}")
            return
        
        try:
            with open(csv_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                self.ampere_test_data = list(reader)
                
                # Update test_status dict for compatibility
                for row in self.ampere_test_data:
                    key = f"{row['model_name']}_{row['quantization_format']}"
                    self.test_status[key] = row['test_status']
                    
            print(f"Loaded {len(self.ampere_test_data)} records from CSV")
        except Exception as e:
            print(f"Error loading CSV: {e}")

    def download_log(self, model: str, quantization_format: str):
        """Download log for specific model and quantization format."""
        status = self.get_test_status(model, quantization_format)
        
        # Try to find log path from CSV data
        log_path = None
        for row in self.ampere_test_data:
            if row['model_name'] == model and row['quantization_format'] == quantization_format:
                log_path = row.get('log_path', '')
                break
        
        # Generate log content
        log_content = f"""Quantization Log
=================
Model: {model}
Quantization Format: {quantization_format}
ModelOpt Version: {self.selected_modelopt_version}
GPU: {self.selected_gpu}
Test Status: {status.upper()}
Log Path: {log_path or 'N/A'}
Timestamp: 2025-01-15 10:30:00

Status: Completed
"""
        # Create download filename
        filename = f"{model}_{quantization_format}.log"
        return rx.download(data=log_content, filename=filename)
