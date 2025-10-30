"""Application state."""
import reflex as rx
import csv
import os
from pathlib import Path


class State(rx.State):
    """Application state."""
    selected_modelopt_version: str = "0.39.0"
    selected_cpu_arch: str = "x86_64"
    selected_gpu: str = "H200"
    selected_model: str = "Llama-3.1-8B-Instruct"
    selected_quantization: str = "fp8"
    
    # Ampere test results data
    ampere_test_data: list[dict] = []
    ampere_test_models: list[str] = []
    ampere_quantization_formats: list[str] = ["int8_sq", "int4_awq"]
    
    # Ada test results data
    ada_test_data: list[dict] = []
    ada_test_models: list[str] = []
    ada_quantization_formats: list[str] = ["fp8", "int8_sq", "int4_awq", "w4a8_awq"]
    
    # Hopper test results data
    hopper_test_data: list[dict] = []
    hopper_test_models: list[str] = []
    hopper_quantization_formats: list[str] = ["fp8", "int8_sq", "int4_awq", "w4a8_awq"]
    
    # Blackwell test results data
    blackwell_test_data: list[dict] = []
    blackwell_test_models: list[str] = []
    blackwell_quantization_formats: list[str] = ["fp8", "nvfp4"]
    
    # Test status, fetch from CSV.
    test_status: dict[str, str] = {}

    def set_modelopt_version(self, version: str):
        """Set the selected ModelOpt version."""
        self.selected_modelopt_version = version
    
    def set_cpu_arch(self, arch: str):
        """Set the selected CPU architecture."""
        self.selected_cpu_arch = arch

    def set_modelopt_version_and_reload_ampere(self, version: str):
        """Set the selected ModelOpt version and reload Ampere data."""
        self.selected_modelopt_version = version
        self.load_ampere_data()
    
    def set_cpu_arch_and_reload_ampere(self, arch: str):
        """Set the selected CPU architecture and reload Ampere data."""
        self.selected_cpu_arch = arch
        self.load_ampere_data()
    
    def set_modelopt_version_and_reload_ada(self, version: str):
        """Set the selected ModelOpt version and reload Ada data."""
        self.selected_modelopt_version = version
        self.load_ada_data()
    
    def set_cpu_arch_and_reload_ada(self, arch: str):
        """Set the selected CPU architecture and reload Ada data."""
        self.selected_cpu_arch = arch
        self.load_ada_data()
    
    def set_modelopt_version_and_reload_hopper(self, version: str):
        """Set the selected ModelOpt version and reload Hopper data."""
        self.selected_modelopt_version = version
        self.load_hopper_data()
    
    def set_cpu_arch_and_reload_hopper(self, arch: str):
        """Set the selected CPU architecture and reload Hopper data."""
        self.selected_cpu_arch = arch
        self.load_hopper_data()
    
    def set_modelopt_version_and_reload_blackwell(self, version: str):
        """Set the selected ModelOpt version and reload Blackwell data."""
        self.selected_modelopt_version = version
        self.load_blackwell_data()
    
    def set_cpu_arch_and_reload_blackwell(self, arch: str):
        """Set the selected CPU architecture and reload Blackwell data."""
        self.selected_cpu_arch = arch
        self.load_blackwell_data()

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
        """Load Ampere test results from TXT file."""
        # First load model list
        models_txt_path = Path(__file__).parent / "config" / "ampere_test_models.txt"
        if models_txt_path.exists():
            try:
                with open(models_txt_path, 'r', encoding='utf-8') as f:
                    self.ampere_test_models = [line.strip() for line in f if line.strip()]
                print(f"Loaded {len(self.ampere_test_models)} models from ampere_test_models.txt")
            except Exception as e:
                print(f"Error loading model list: {e}")
        
        # Initialize all model+quantization combinations as NA (not available)
        for model in self.ampere_test_models:
            for qformat in self.ampere_quantization_formats:
                key = f"{model}_{qformat}"
                self.test_status[key] = "NA"
        
        # Then load test results
        csv_path = Path(__file__).parent / "data" / "ampere_quantization_test_results.csv"
        
        if not csv_path.exists():
            print(f"CSV file not found: {csv_path}")
            return
        
        try:
            with open(csv_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                all_data = list(reader)
                
                # Filter by selected ModelOpt version and CPU architecture
                self.ampere_test_data = [
                    row for row in all_data 
                    if row.get('modelopt_version', '0.39.0') == self.selected_modelopt_version
                    and row.get('cpu_arch', 'x86_64') == self.selected_cpu_arch
                ]
                
                # Update test_status dict with actual test results
                # This will override the unsupported status for models that have test results
                for row in self.ampere_test_data:
                    key = f"{row['model_name']}_{row['quantization_format']}"
                    self.test_status[key] = row['test_status']
                    
            print(f"Loaded {len(self.ampere_test_data)} Ampere records for version {self.selected_modelopt_version}")
        except Exception as e:
            print(f"Error loading CSV: {e}")

    def load_ada_data(self):
        """Load Ada test results from TXT file."""
        # First load model list
        models_txt_path = Path(__file__).parent / "config" / "ada_test_models.txt"
        if models_txt_path.exists():
            try:
                with open(models_txt_path, 'r', encoding='utf-8') as f:
                    self.ada_test_models = [line.strip() for line in f if line.strip()]
                print(f"Loaded {len(self.ada_test_models)} models from ada_test_models.txt")
            except Exception as e:
                print(f"Error loading model list: {e}")
        
        # Initialize all model+quantization combinations as NA (not available)
        for model in self.ada_test_models:
            for qformat in self.ada_quantization_formats:
                key = f"{model}_{qformat}"
                self.test_status[key] = "NA"
        
        # Then load test results
        csv_path = Path(__file__).parent / "data" / "ada_quantization_test_results.csv"
        
        if not csv_path.exists():
            print(f"CSV file not found: {csv_path}")
            return
        
        try:
            with open(csv_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                all_data = list(reader)
                
                # Filter by selected ModelOpt version and CPU architecture
                self.ada_test_data = [
                    row for row in all_data 
                    if row.get('modelopt_version', '0.39.0') == self.selected_modelopt_version
                    and row.get('cpu_arch', 'x86_64') == self.selected_cpu_arch
                ]
                
                # Update test_status dict with actual test results
                # This will override the NA status for models that have test results
                for row in self.ada_test_data:
                    key = f"{row['model_name']}_{row['quantization_format']}"
                    self.test_status[key] = row['test_status']
                    
            print(f"Loaded {len(self.ada_test_data)} Ada records for version {self.selected_modelopt_version}")
        except Exception as e:
            print(f"Error loading Ada CSV: {e}")

    def load_hopper_data(self):
        """Load Hopper test results from TXT file."""
        # First load model list
        models_txt_path = Path(__file__).parent / "config" / "hopper_test_models.txt"
        if models_txt_path.exists():
            try:
                with open(models_txt_path, 'r', encoding='utf-8') as f:
                    self.hopper_test_models = [line.strip() for line in f if line.strip()]
                print(f"Loaded {len(self.hopper_test_models)} models from hopper_test_models.txt")
            except Exception as e:
                print(f"Error loading model list: {e}")
        
        # Initialize all model+quantization combinations as NA (not available)
        for model in self.hopper_test_models:
            for qformat in self.hopper_quantization_formats:
                key = f"{model}_{qformat}"
                self.test_status[key] = "NA"
        
        # Then load test results
        csv_path = Path(__file__).parent / "data" / "hopper_quantization_test_results.csv"
        
        if not csv_path.exists():
            print(f"CSV file not found: {csv_path}")
            return
        
        try:
            with open(csv_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                all_data = list(reader)
                
                # Filter by selected ModelOpt version and CPU architecture
                self.hopper_test_data = [
                    row for row in all_data 
                    if row.get('modelopt_version', '0.39.0') == self.selected_modelopt_version
                    and row.get('cpu_arch', 'x86_64') == self.selected_cpu_arch
                ]
                
                # Update test_status dict with actual test results
                # This will override the NA status for models that have test results
                for row in self.hopper_test_data:
                    key = f"{row['model_name']}_{row['quantization_format']}"
                    self.test_status[key] = row['test_status']
                    
            print(f"Loaded {len(self.hopper_test_data)} Hopper records for version {self.selected_modelopt_version}")
        except Exception as e:
            print(f"Error loading Hopper CSV: {e}")

    def load_blackwell_data(self):
        """Load Blackwell test results from TXT file."""
        # First load model list
        models_txt_path = Path(__file__).parent / "config" / "blackwell_test_models.txt"
        if models_txt_path.exists():
            try:
                with open(models_txt_path, 'r', encoding='utf-8') as f:
                    self.blackwell_test_models = [line.strip() for line in f if line.strip()]
                print(f"Loaded {len(self.blackwell_test_models)} models from blackwell_test_models.txt")
            except Exception as e:
                print(f"Error loading model list: {e}")
        
        # Initialize all model+quantization combinations as NA (not available)
        for model in self.blackwell_test_models:
            for qformat in self.blackwell_quantization_formats:
                key = f"{model}_{qformat}"
                self.test_status[key] = "NA"
        
        # Then load test results
        csv_path = Path(__file__).parent / "data" / "blackwell_quantization_test_results.csv"
        
        if not csv_path.exists():
            print(f"CSV file not found: {csv_path}")
            return
        
        try:
            with open(csv_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                all_data = list(reader)
                
                # Filter by selected ModelOpt version and CPU architecture
                self.blackwell_test_data = [
                    row for row in all_data 
                    if row.get('modelopt_version', '0.39.0') == self.selected_modelopt_version
                    and row.get('cpu_arch', 'x86_64') == self.selected_cpu_arch
                ]
                
                # Update test_status dict with actual test results
                # This will override the NA status for models that have test results
                for row in self.blackwell_test_data:
                    key = f"{row['model_name']}_{row['quantization_format']}"
                    self.test_status[key] = row['test_status']
                    
            print(f"Loaded {len(self.blackwell_test_data)} Blackwell records for version {self.selected_modelopt_version}")
        except Exception as e:
            print(f"Error loading Blackwell CSV: {e}")

    def download_log(self, model: str, quantization_format: str):
        """Download log for specific model and quantization format."""
        status = self.get_test_status(model, quantization_format)
        
        # Try to find log path from CSV data (check all architecture data)
        log_path = None
        for row in self.ampere_test_data + self.ada_test_data + self.hopper_test_data + self.blackwell_test_data:
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
