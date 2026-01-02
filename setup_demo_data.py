import yaml
import os

def setup():
    config = {
        "sectors": {
            "default": {
                "weights": {
                    "earnings_quality": 0.5,
                    "working_capital": 0.2,
                    "nlp": 0.3
                }
            }
        }
    }
    
    os.makedirs("data", exist_ok=True)
    with open("data/sector_config.yaml", "w") as f:
        yaml.dump(config, f)
    
    print("[+] Demo configuration created in data/sector_config.yaml")

if __name__ == "__main__":
    setup()
