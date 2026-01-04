import yaml
from typing import Dict, Any

class ConfigLoader:
    @staticmethod
    def load_sector_config(path: str) -> Dict[str, Any]:
        try:
            with open(path, 'r') as f:
                return yaml.safe_load(f)
        except FileNotFoundError:
            return {"sectors": {"default": {"weights": {"earnings_quality": 0.5, "working_capital": 0.2, "nlp": 0.3}}}}
