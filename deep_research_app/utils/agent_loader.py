import yaml
from pathlib import Path

CONFIG_PATH = Path(__file__).resolve().parents[1] / "config" / "agents.yaml"


def load_agents_config():
    with open(CONFIG_PATH, "r") as f:
        config = yaml.safe_load(f)

    return config["agents"]