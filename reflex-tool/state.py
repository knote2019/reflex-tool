"""Application state."""
import reflex as rx
import csv
from pathlib import Path


class State(rx.State):
    """Application state."""
    selected_modelopt_version: str = "0.39.0"
    selected_cpu_arch: str = "x86_64"
    selected_gpu: str = "H200"
    selected_model: str = "Llama-3.1-8B-Instruct"
    selected_quantization: str = "fp8"
    
    # Cache flags to prevent redundant data loading
    _ampere_quantization_loaded: bool = False
    _ada_quantization_loaded: bool = False
    _hopper_quantization_loaded: bool = False
    _blackwell_quantization_loaded: bool = False
    _ampere_inference_loaded: bool = False
    _ada_inference_loaded: bool = False
    _hopper_inference_loaded: bool = False
    _blackwell_inference_loaded: bool = False
    _ampere_performance_loaded: bool = False
    _ada_performance_loaded: bool = False
    _hopper_performance_loaded: bool = False
    _blackwell_performance_loaded: bool = False
    
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
    
    # Ampere inference test results data
    ampere_inference_test_data: list[dict] = []
    
    # Ada inference test results data
    ada_inference_test_data: list[dict] = []
    
    # Hopper inference test results data
    hopper_inference_test_data: list[dict] = []
    
    # Blackwell inference test results data
    blackwell_inference_test_data: list[dict] = []
    
    # Test status, fetch from CSV.
    test_status: dict[str, str] = {}
    
    # Inference test status
    inference_test_status: dict[str, str] = {}
    
    # Performance test status
    performance_test_status: dict[str, str] = {}
    
    # Model management state
    selected_architecture: str = "ampere"
    new_model_name: str = ""
    is_editing_models: bool = False
    model_to_delete: str = ""
    show_delete_confirm: bool = False

    def set_modelopt_version(self, version: str):
        """Set the selected ModelOpt version."""
        self.selected_modelopt_version = version
    
    def set_cpu_arch(self, arch: str):
        """Set the selected CPU architecture."""
        self.selected_cpu_arch = arch

    def set_modelopt_version_and_reload_ampere(self, version: str):
        """Set the selected ModelOpt version and reload Ampere data."""
        self.selected_modelopt_version = version
        self._ampere_quantization_loaded = False
        self.load_ampere_data()
    
    def set_cpu_arch_and_reload_ampere(self, arch: str):
        """Set the selected CPU architecture and reload Ampere data."""
        self.selected_cpu_arch = arch
        self._ampere_quantization_loaded = False
        self.load_ampere_data()
    
    def set_modelopt_version_and_reload_ada(self, version: str):
        """Set the selected ModelOpt version and reload Ada data."""
        self.selected_modelopt_version = version
        self._ada_quantization_loaded = False
        self.load_ada_data()
    
    def set_cpu_arch_and_reload_ada(self, arch: str):
        """Set the selected CPU architecture and reload Ada data."""
        self.selected_cpu_arch = arch
        self._ada_quantization_loaded = False
        self.load_ada_data()
    
    def set_modelopt_version_and_reload_hopper(self, version: str):
        """Set the selected ModelOpt version and reload Hopper data."""
        self.selected_modelopt_version = version
        self._hopper_quantization_loaded = False
        self.load_hopper_data()
    
    def set_cpu_arch_and_reload_hopper(self, arch: str):
        """Set the selected CPU architecture and reload Hopper data."""
        self.selected_cpu_arch = arch
        self._hopper_quantization_loaded = False
        self.load_hopper_data()
    
    def set_modelopt_version_and_reload_blackwell(self, version: str):
        """Set the selected ModelOpt version and reload Blackwell data."""
        self.selected_modelopt_version = version
        self._blackwell_quantization_loaded = False
        self.load_blackwell_data()
    
    def set_cpu_arch_and_reload_blackwell(self, arch: str):
        """Set the selected CPU architecture and reload Blackwell data."""
        self.selected_cpu_arch = arch
        self._blackwell_quantization_loaded = False
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

    def refresh_ampere_data(self):
        """Refresh Ampere data and show toast."""
        self._ampere_quantization_loaded = False
        self.load_ampere_data()
        yield rx.toast.success("Data refreshed successfully")
    
    def refresh_ada_data(self):
        """Refresh Ada data and show toast."""
        self._ada_quantization_loaded = False
        self.load_ada_data()
        yield rx.toast.success("Data refreshed successfully")
    
    def refresh_hopper_data(self):
        """Refresh Hopper data and show toast."""
        self._hopper_quantization_loaded = False
        self.load_hopper_data()
        yield rx.toast.success("Data refreshed successfully")
    
    def refresh_blackwell_data(self):
        """Refresh Blackwell data and show toast."""
        self._blackwell_quantization_loaded = False
        self.load_blackwell_data()
        yield rx.toast.success("Data refreshed successfully")
    
    def refresh_ampere_inference_data(self):
        """Refresh Ampere inference data and show toast."""
        self._ampere_inference_loaded = False
        self.load_ampere_inference_data()
        yield rx.toast.success("Data refreshed successfully")
    
    def refresh_ada_inference_data(self):
        """Refresh Ada inference data and show toast."""
        self._ada_inference_loaded = False
        self.load_ada_inference_data()
        yield rx.toast.success("Data refreshed successfully")
    
    def refresh_hopper_inference_data(self):
        """Refresh Hopper inference data and show toast."""
        self._hopper_inference_loaded = False
        self.load_hopper_inference_data()
        yield rx.toast.success("Data refreshed successfully")
    
    def refresh_blackwell_inference_data(self):
        """Refresh Blackwell inference data and show toast."""
        self._blackwell_inference_loaded = False
        self.load_blackwell_inference_data()
        yield rx.toast.success("Data refreshed successfully")
    
    def refresh_ampere_performance_data(self):
        """Refresh Ampere performance data and show toast."""
        self._ampere_performance_loaded = False
        self.load_ampere_performance_data()
        yield rx.toast.success("Data refreshed successfully")
    
    def refresh_ada_performance_data(self):
        """Refresh Ada performance data and show toast."""
        self._ada_performance_loaded = False
        self.load_ada_performance_data()
        yield rx.toast.success("Data refreshed successfully")
    
    def refresh_hopper_performance_data(self):
        """Refresh Hopper performance data and show toast."""
        self._hopper_performance_loaded = False
        self.load_hopper_performance_data()
        yield rx.toast.success("Data refreshed successfully")
    
    def refresh_blackwell_performance_data(self):
        """Refresh Blackwell performance data and show toast."""
        self._blackwell_performance_loaded = False
        self.load_blackwell_performance_data()
        yield rx.toast.success("Data refreshed successfully")

    def get_test_status(self, model: str, quantization_format: str) -> str:
        """Get test status for specific model and quantization format."""
        key = f"{model}_{quantization_format}"
        return self.test_status.get(key, "passed")  # Default to passed

    def load_ampere_data(self):
        """Load Ampere test results from TXT file."""
        # Return if already loaded (use cache)
        if self._ampere_quantization_loaded:
            return
        
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
            self._ampere_quantization_loaded = True
        except Exception as e:
            print(f"Error loading CSV: {e}")

    def load_ada_data(self):
        """Load Ada test results from TXT file."""
        # Return if already loaded (use cache)
        if self._ada_quantization_loaded:
            return
        
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
            self._ada_quantization_loaded = True
        except Exception as e:
            print(f"Error loading Ada CSV: {e}")

    def load_hopper_data(self):
        """Load Hopper test results from TXT file."""
        # Return if already loaded (use cache)
        if self._hopper_quantization_loaded:
            return
        
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
            self._hopper_quantization_loaded = True
        except Exception as e:
            print(f"Error loading Hopper CSV: {e}")

    def load_blackwell_data(self):
        """Load Blackwell test results from TXT file."""
        # Return if already loaded (use cache)
        if self._blackwell_quantization_loaded:
            return
        
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
            self._blackwell_quantization_loaded = True
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
        filename = f"{model}_{quantization_format}_quantization.log"
        return rx.download(data=log_content, filename=filename)
    
    def get_inference_test_status(self, model: str, quantization_format: str) -> str:
        """Get inference test status for specific model and quantization format."""
        key = f"{model}_{quantization_format}"
        return self.inference_test_status.get(key, "NA")  # Default to NA
    
    def set_modelopt_version_and_reload_ampere_inference(self, version: str):
        """Set the selected ModelOpt version and reload Ampere inference data."""
        self.selected_modelopt_version = version
        self._ampere_inference_loaded = False
        self.load_ampere_inference_data()
    
    def set_cpu_arch_and_reload_ampere_inference(self, arch: str):
        """Set the selected CPU architecture and reload Ampere inference data."""
        self.selected_cpu_arch = arch
        self._ampere_inference_loaded = False
        self.load_ampere_inference_data()
    
    def set_modelopt_version_and_reload_ada_inference(self, version: str):
        """Set the selected ModelOpt version and reload Ada inference data."""
        self.selected_modelopt_version = version
        self._ada_inference_loaded = False
        self.load_ada_inference_data()
    
    def set_cpu_arch_and_reload_ada_inference(self, arch: str):
        """Set the selected CPU architecture and reload Ada inference data."""
        self.selected_cpu_arch = arch
        self._ada_inference_loaded = False
        self.load_ada_inference_data()
    
    def set_modelopt_version_and_reload_hopper_inference(self, version: str):
        """Set the selected ModelOpt version and reload Hopper inference data."""
        self.selected_modelopt_version = version
        self._hopper_inference_loaded = False
        self.load_hopper_inference_data()
    
    def set_cpu_arch_and_reload_hopper_inference(self, arch: str):
        """Set the selected CPU architecture and reload Hopper inference data."""
        self.selected_cpu_arch = arch
        self._hopper_inference_loaded = False
        self.load_hopper_inference_data()
    
    def set_modelopt_version_and_reload_blackwell_inference(self, version: str):
        """Set the selected ModelOpt version and reload Blackwell inference data."""
        self.selected_modelopt_version = version
        self._blackwell_inference_loaded = False
        self.load_blackwell_inference_data()
    
    def set_cpu_arch_and_reload_blackwell_inference(self, arch: str):
        """Set the selected CPU architecture and reload Blackwell inference data."""
        self.selected_cpu_arch = arch
        self._blackwell_inference_loaded = False
        self.load_blackwell_inference_data()
    
    def load_ampere_inference_data(self):
        """Load Ampere inference test results from CSV file."""
        # Return if already loaded (use cache)
        if self._ampere_inference_loaded:
            return
        
        # First load model list if not already loaded
        if not self.ampere_test_models:
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
                self.inference_test_status[key] = "NA"
        
        # Load inference test results
        csv_path = Path(__file__).parent / "data" / "ampere_inference_test_results.csv"
        
        if not csv_path.exists():
            print(f"Inference CSV file not found: {csv_path}")
            return
        
        try:
            with open(csv_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                all_data = list(reader)
                
                # Filter by selected ModelOpt version and CPU architecture
                self.ampere_inference_test_data = [
                    row for row in all_data 
                    if row.get('modelopt_version', '0.39.0') == self.selected_modelopt_version
                    and row.get('cpu_arch', 'x86_64') == self.selected_cpu_arch
                ]
                
                # Update inference_test_status dict with actual test results
                for row in self.ampere_inference_test_data:
                    key = f"{row['model_name']}_{row['quantization_format']}"
                    self.inference_test_status[key] = row['test_status']
                    
            print(f"Loaded {len(self.ampere_inference_test_data)} Ampere inference records for version {self.selected_modelopt_version}")
            self._ampere_inference_loaded = True
        except Exception as e:
            print(f"Error loading Ampere inference CSV: {e}")
    
    def download_inference_log(self, model: str, quantization_format: str):
        """Download inference log for specific model and quantization format."""
        status = self.get_inference_test_status(model, quantization_format)
        
        # Try to find log path from CSV data
        log_path = None
        for row in self.ampere_inference_test_data + self.ada_inference_test_data + self.hopper_inference_test_data + self.blackwell_inference_test_data:
            if row['model_name'] == model and row['quantization_format'] == quantization_format:
                log_path = row.get('log_path', '')
                break
        
        # Generate log content
        log_content = f"""Inference Log
=================
Model: {model}
Quantization Format: {quantization_format}
ModelOpt Version: {self.selected_modelopt_version}
CPU Arch: {self.selected_cpu_arch}
Test Status: {status.upper()}
Log Path: {log_path or 'N/A'}
Timestamp: 2025-01-15 10:30:00

Status: Completed
"""
        # Create download filename
        filename = f"{model}_{quantization_format}_inference.log"
        return rx.download(data=log_content, filename=filename)
    
    def load_ada_inference_data(self):
        """Load Ada inference test results from CSV file."""
        # Return if already loaded (use cache)
        if self._ada_inference_loaded:
            return
        
        # First load model list if not already loaded
        if not self.ada_test_models:
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
                self.inference_test_status[key] = "NA"
        
        # Load inference test results
        csv_path = Path(__file__).parent / "data" / "ada_inference_test_results.csv"
        
        if not csv_path.exists():
            print(f"Inference CSV file not found: {csv_path}")
            return
        
        try:
            with open(csv_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                all_data = list(reader)
                
                # Filter by selected ModelOpt version and CPU architecture
                self.ada_inference_test_data = [
                    row for row in all_data 
                    if row.get('modelopt_version', '0.39.0') == self.selected_modelopt_version
                    and row.get('cpu_arch', 'x86_64') == self.selected_cpu_arch
                ]
                
                # Update inference_test_status dict with actual test results
                for row in self.ada_inference_test_data:
                    key = f"{row['model_name']}_{row['quantization_format']}"
                    self.inference_test_status[key] = row['test_status']
                    
            print(f"Loaded {len(self.ada_inference_test_data)} Ada inference records for version {self.selected_modelopt_version}")
            self._ada_inference_loaded = True
        except Exception as e:
            print(f"Error loading Ada inference CSV: {e}")
    
    def load_hopper_inference_data(self):
        """Load Hopper inference test results from CSV file."""
        # Return if already loaded (use cache)
        if self._hopper_inference_loaded:
            return
        
        # First load model list if not already loaded
        if not self.hopper_test_models:
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
                self.inference_test_status[key] = "NA"
        
        # Load inference test results
        csv_path = Path(__file__).parent / "data" / "hopper_inference_test_results.csv"
        
        if not csv_path.exists():
            print(f"Inference CSV file not found: {csv_path}")
            return
        
        try:
            with open(csv_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                all_data = list(reader)
                
                # Filter by selected ModelOpt version and CPU architecture
                self.hopper_inference_test_data = [
                    row for row in all_data 
                    if row.get('modelopt_version', '0.39.0') == self.selected_modelopt_version
                    and row.get('cpu_arch', 'x86_64') == self.selected_cpu_arch
                ]
                
                # Update inference_test_status dict with actual test results
                for row in self.hopper_inference_test_data:
                    key = f"{row['model_name']}_{row['quantization_format']}"
                    self.inference_test_status[key] = row['test_status']
                    
            print(f"Loaded {len(self.hopper_inference_test_data)} Hopper inference records for version {self.selected_modelopt_version}")
            self._hopper_inference_loaded = True
        except Exception as e:
            print(f"Error loading Hopper inference CSV: {e}")
    
    def load_blackwell_inference_data(self):
        """Load Blackwell inference test results from CSV file."""
        # Return if already loaded (use cache)
        if self._blackwell_inference_loaded:
            return
        
        # First load model list if not already loaded
        if not self.blackwell_test_models:
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
                self.inference_test_status[key] = "NA"
        
        # Load inference test results
        csv_path = Path(__file__).parent / "data" / "blackwell_inference_test_results.csv"
        
        if not csv_path.exists():
            print(f"Inference CSV file not found: {csv_path}")
            return
        
        try:
            with open(csv_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                all_data = list(reader)
                
                # Filter by selected ModelOpt version and CPU architecture
                self.blackwell_inference_test_data = [
                    row for row in all_data 
                    if row.get('modelopt_version', '0.39.0') == self.selected_modelopt_version
                    and row.get('cpu_arch', 'x86_64') == self.selected_cpu_arch
                ]
                
                # Update inference_test_status dict with actual test results
                for row in self.blackwell_inference_test_data:
                    key = f"{row['model_name']}_{row['quantization_format']}"
                    self.inference_test_status[key] = row['test_status']
                    
            print(f"Loaded {len(self.blackwell_inference_test_data)} Blackwell inference records for version {self.selected_modelopt_version}")
            self._blackwell_inference_loaded = True
        except Exception as e:
            print(f"Error loading Blackwell inference CSV: {e}")
    
    # Performance-related methods
    def set_modelopt_version_and_reload_ampere_performance(self, version: str):
        """Set the selected ModelOpt version and reload Ampere performance data."""
        self.selected_modelopt_version = version
        self._ampere_performance_loaded = False
        self.load_ampere_performance_data()
    
    def set_cpu_arch_and_reload_ampere_performance(self, arch: str):
        """Set the selected CPU architecture and reload Ampere performance data."""
        self.selected_cpu_arch = arch
        self._ampere_performance_loaded = False
        self.load_ampere_performance_data()
    
    def set_modelopt_version_and_reload_ada_performance(self, version: str):
        """Set the selected ModelOpt version and reload Ada performance data."""
        self.selected_modelopt_version = version
        self._ada_performance_loaded = False
        self.load_ada_performance_data()
    
    def set_cpu_arch_and_reload_ada_performance(self, arch: str):
        """Set the selected CPU architecture and reload Ada performance data."""
        self.selected_cpu_arch = arch
        self._ada_performance_loaded = False
        self.load_ada_performance_data()
    
    def set_modelopt_version_and_reload_hopper_performance(self, version: str):
        """Set the selected ModelOpt version and reload Hopper performance data."""
        self.selected_modelopt_version = version
        self._hopper_performance_loaded = False
        self.load_hopper_performance_data()
    
    def set_cpu_arch_and_reload_hopper_performance(self, arch: str):
        """Set the selected CPU architecture and reload Hopper performance data."""
        self.selected_cpu_arch = arch
        self._hopper_performance_loaded = False
        self.load_hopper_performance_data()
    
    def set_modelopt_version_and_reload_blackwell_performance(self, version: str):
        """Set the selected ModelOpt version and reload Blackwell performance data."""
        self.selected_modelopt_version = version
        self._blackwell_performance_loaded = False
        self.load_blackwell_performance_data()
    
    def set_cpu_arch_and_reload_blackwell_performance(self, arch: str):
        """Set the selected CPU architecture and reload Blackwell performance data."""
        self.selected_cpu_arch = arch
        self._blackwell_performance_loaded = False
        self.load_blackwell_performance_data()
    
    def load_ampere_performance_data(self):
        """Load Ampere performance test results from CSV file."""
        # Return if already loaded (use cache)
        if self._ampere_performance_loaded:
            return
        
        # First load model list if not already loaded
        if not self.ampere_test_models:
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
                self.performance_test_status[key] = "NA"
        
        # Load performance test results
        csv_path = Path(__file__).parent / "data" / "ampere_performance_test_results.csv"
        
        if not csv_path.exists():
            print(f"Performance CSV file not found: {csv_path}")
            return
        
        try:
            with open(csv_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                all_data = list(reader)
                
                # Filter by selected ModelOpt version and CPU architecture
                ampere_performance_data = [
                    row for row in all_data 
                    if row.get('modelopt_version', '0.39.0') == self.selected_modelopt_version
                    and row.get('cpu_arch', 'x86_64') == self.selected_cpu_arch
                ]
                
                # Update performance_test_status dict with actual test results
                for row in ampere_performance_data:
                    key = f"{row['model_name']}_{row['quantization_format']}"
                    self.performance_test_status[key] = row['test_status']
                    
            print(f"Loaded {len(ampere_performance_data)} Ampere performance records for version {self.selected_modelopt_version}")
            self._ampere_performance_loaded = True
        except Exception as e:
            print(f"Error loading Ampere performance CSV: {e}")
    
    def load_ada_performance_data(self):
        """Load Ada performance test results from CSV file."""
        # Return if already loaded (use cache)
        if self._ada_performance_loaded:
            return
        
        # First load model list if not already loaded
        if not self.ada_test_models:
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
                self.performance_test_status[key] = "NA"
        
        # Load performance test results
        csv_path = Path(__file__).parent / "data" / "ada_performance_test_results.csv"
        
        if not csv_path.exists():
            print(f"Performance CSV file not found: {csv_path}")
            return
        
        try:
            with open(csv_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                all_data = list(reader)
                
                # Filter by selected ModelOpt version and CPU architecture
                ada_performance_data = [
                    row for row in all_data 
                    if row.get('modelopt_version', '0.39.0') == self.selected_modelopt_version
                    and row.get('cpu_arch', 'x86_64') == self.selected_cpu_arch
                ]
                
                # Update performance_test_status dict with actual test results
                for row in ada_performance_data:
                    key = f"{row['model_name']}_{row['quantization_format']}"
                    self.performance_test_status[key] = row['test_status']
                    
            print(f"Loaded {len(ada_performance_data)} Ada performance records for version {self.selected_modelopt_version}")
            self._ada_performance_loaded = True
        except Exception as e:
            print(f"Error loading Ada performance CSV: {e}")
    
    def load_hopper_performance_data(self):
        """Load Hopper performance test results from CSV file."""
        # Return if already loaded (use cache)
        if self._hopper_performance_loaded:
            return
        
        # First load model list if not already loaded
        if not self.hopper_test_models:
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
                self.performance_test_status[key] = "NA"
        
        # Load performance test results
        csv_path = Path(__file__).parent / "data" / "hopper_performance_test_results.csv"
        
        if not csv_path.exists():
            print(f"Performance CSV file not found: {csv_path}")
            return
        
        try:
            with open(csv_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                all_data = list(reader)
                
                # Filter by selected ModelOpt version and CPU architecture
                hopper_performance_data = [
                    row for row in all_data 
                    if row.get('modelopt_version', '0.39.0') == self.selected_modelopt_version
                    and row.get('cpu_arch', 'x86_64') == self.selected_cpu_arch
                ]
                
                # Update performance_test_status dict with actual test results
                for row in hopper_performance_data:
                    key = f"{row['model_name']}_{row['quantization_format']}"
                    self.performance_test_status[key] = row['test_status']
                    
            print(f"Loaded {len(hopper_performance_data)} Hopper performance records for version {self.selected_modelopt_version}")
            self._hopper_performance_loaded = True
        except Exception as e:
            print(f"Error loading Hopper performance CSV: {e}")
    
    def load_blackwell_performance_data(self):
        """Load Blackwell performance test results from CSV file."""
        # Return if already loaded (use cache)
        if self._blackwell_performance_loaded:
            return
        
        # First load model list if not already loaded
        if not self.blackwell_test_models:
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
                self.performance_test_status[key] = "NA"
        
        # Load performance test results
        csv_path = Path(__file__).parent / "data" / "blackwell_performance_test_results.csv"
        
        if not csv_path.exists():
            print(f"Performance CSV file not found: {csv_path}")
            return
        
        try:
            with open(csv_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                all_data = list(reader)
                
                # Filter by selected ModelOpt version and CPU architecture
                blackwell_performance_data = [
                    row for row in all_data 
                    if row.get('modelopt_version', '0.39.0') == self.selected_modelopt_version
                    and row.get('cpu_arch', 'x86_64') == self.selected_cpu_arch
                ]
                
                # Update performance_test_status dict with actual test results
                for row in blackwell_performance_data:
                    key = f"{row['model_name']}_{row['quantization_format']}"
                    self.performance_test_status[key] = row['test_status']
                    
            print(f"Loaded {len(blackwell_performance_data)} Blackwell performance records for version {self.selected_modelopt_version}")
            self._blackwell_performance_loaded = True
        except Exception as e:
            print(f"Error loading Blackwell performance CSV: {e}")
    
    def download_performance_log(self, model: str, quantization_format: str):
        """Download performance log for specific model and quantization format."""
        status = self.performance_test_status.get(f"{model}_{quantization_format}", "NA")
        
        # Generate log content
        log_content = f"""Performance Log
=================
Model: {model}
Quantization Format: {quantization_format}
ModelOpt Version: {self.selected_modelopt_version}
CPU Arch: {self.selected_cpu_arch}
Test Status: {status.upper()}
Timestamp: 2025-01-15 10:30:00

Status: Completed
"""
        # Create download filename
        filename = f"{model}_{quantization_format}_performance.log"
        return rx.download(data=log_content, filename=filename)
    
    # Model management methods
    def set_selected_architecture(self, arch: str):
        """Set the selected architecture for model management."""
        # Convert to lowercase for internal use
        arch_lower = arch.lower()
        self.selected_architecture = arch_lower
        # Load data for the newly selected architecture
        if arch_lower == "ampere":
            self.load_ampere_data()
        elif arch_lower == "ada":
            self.load_ada_data()
        elif arch_lower == "hopper":
            self.load_hopper_data()
        elif arch_lower == "blackwell":
            self.load_blackwell_data()
    
    def set_new_model_name(self, name: str):
        """Set the new model name."""
        self.new_model_name = name
    
    def toggle_edit_mode(self):
        """Toggle the edit mode for model management."""
        self.is_editing_models = not self.is_editing_models
        # Clear input when exiting edit mode
        if not self.is_editing_models:
            self.new_model_name = ""
    
    def reset_edit_mode(self):
        """Reset edit mode to non-editing state."""
        self.is_editing_models = False
        self.new_model_name = ""
        self.model_to_delete = ""
        self.show_delete_confirm = False
    
    def open_delete_confirm(self, model_name: str):
        """Open the delete confirmation dialog."""
        self.model_to_delete = model_name
        self.show_delete_confirm = True
    
    def close_delete_confirm(self):
        """Close the delete confirmation dialog."""
        self.show_delete_confirm = False
        self.model_to_delete = ""
    
    def confirm_delete_model(self):
        """Confirm and delete the selected model."""
        if self.model_to_delete:
            self.remove_model_from_architecture(self.model_to_delete)
        self.show_delete_confirm = False
        self.model_to_delete = ""
    
    @rx.var
    def current_architecture_models(self) -> list[str]:
        """Get the model list for the currently selected architecture."""
        if self.selected_architecture == "ampere":
            return self.ampere_test_models
        elif self.selected_architecture == "ada":
            return self.ada_test_models
        elif self.selected_architecture == "hopper":
            return self.hopper_test_models
        elif self.selected_architecture == "blackwell":
            return self.blackwell_test_models
        return []
    
    def add_model_to_architecture(self):
        """Add a new model to the selected architecture's test_models.txt file."""
        if not self.new_model_name or not self.new_model_name.strip():
            print("Model name cannot be empty")
            return
        
        model_name = self.new_model_name.strip()
        
        # Get the path to the appropriate txt file
        models_txt_path = Path(__file__).parent / "config" / f"{self.selected_architecture}_test_models.txt"
        
        # Read existing models
        existing_models = []
        if models_txt_path.exists():
            try:
                with open(models_txt_path, 'r', encoding='utf-8') as f:
                    existing_models = [line.strip() for line in f if line.strip()]
            except Exception as e:
                print(f"Error reading model list: {e}")
                return
        
        # Check if model already exists
        if model_name in existing_models:
            print(f"Model '{model_name}' already exists in {self.selected_architecture} architecture")
            return
        
        # Add the new model
        existing_models.append(model_name)
        
        # Write back to file
        try:
            with open(models_txt_path, 'w', encoding='utf-8') as f:
                for model in existing_models:
                    f.write(f"{model}\n")
            print(f"✅ Added model '{model_name}' to {self.selected_architecture} architecture")
            
            # Clear the input and reload data
            self.new_model_name = ""
            self._reload_architecture_data()
        except Exception as e:
            print(f"Error writing model list: {e}")
    
    def remove_model_from_architecture(self, model_name: str):
        """Remove a model from the selected architecture's test_models.txt file."""
        if not model_name:
            return
        
        # Get the path to the appropriate txt file
        models_txt_path = Path(__file__).parent / "config" / f"{self.selected_architecture}_test_models.txt"
        
        # Read existing models
        existing_models = []
        if models_txt_path.exists():
            try:
                with open(models_txt_path, 'r', encoding='utf-8') as f:
                    existing_models = [line.strip() for line in f if line.strip()]
            except Exception as e:
                print(f"Error reading model list: {e}")
                return
        
        # Remove the model
        if model_name in existing_models:
            existing_models.remove(model_name)
            
            # Write back to file
            try:
                with open(models_txt_path, 'w', encoding='utf-8') as f:
                    for model in existing_models:
                        f.write(f"{model}\n")
                print(f"✅ Removed model '{model_name}' from {self.selected_architecture} architecture")
                
                # Reload data
                self._reload_architecture_data()
            except Exception as e:
                print(f"Error writing model list: {e}")
        else:
            print(f"Model '{model_name}' not found in {self.selected_architecture} architecture")
    
    def _reload_architecture_data(self):
        """Reload data for the selected architecture."""
        # Clear cache for the selected architecture
        if self.selected_architecture == "ampere":
            self._ampere_quantization_loaded = False
            self._ampere_inference_loaded = False
            self._ampere_performance_loaded = False
            self.load_ampere_data()
        elif self.selected_architecture == "ada":
            self._ada_quantization_loaded = False
            self._ada_inference_loaded = False
            self._ada_performance_loaded = False
            self.load_ada_data()
        elif self.selected_architecture == "hopper":
            self._hopper_quantization_loaded = False
            self._hopper_inference_loaded = False
            self._hopper_performance_loaded = False
            self.load_hopper_data()
        elif self.selected_architecture == "blackwell":
            self._blackwell_quantization_loaded = False
            self._blackwell_inference_loaded = False
            self._blackwell_performance_loaded = False
            self.load_blackwell_data()
