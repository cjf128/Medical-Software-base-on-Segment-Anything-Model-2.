from dataclasses import dataclass
from pathlib import Path

import yaml

BASE_PATH = Path(__file__).resolve().parent.parent


@dataclass
class AppConfig:
    width: int = 900
    height: int = 600


class ConfigManager:
    def __init__(self):
        self.config_file = BASE_PATH / "config.yaml"

    def load(self) -> AppConfig:
        if not self.config_file.exists():
            return AppConfig()

        try:
            with open(self.config_file, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f) or {}

            return AppConfig(
                width=int(data.get("window", {}).get("width", 900)),
                height=int(data.get("window", {}).get("height", 600)),
            )
        except Exception:
            return AppConfig()

    def save(self, config: AppConfig):
        data = {}
        if self.config_file.exists():
            try:
                with open(self.config_file, "r", encoding="utf-8") as f:
                    data = yaml.safe_load(f) or {}
            except Exception:
                pass

        if "window" not in data:
            data["window"] = {}

        data["window"]["width"] = config.width
        data["window"]["height"] = config.height

        with open(self.config_file, "w", encoding="utf-8") as f:
            yaml.safe_dump(data, f, allow_unicode=True)
