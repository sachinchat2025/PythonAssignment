import json
from pathlib import Path


class EnvConfig:
    def __init__(self, path: str = None):
        base = Path(__file__).parent
        cfg_path = Path(path) if path else base / "config.json"
        with open(cfg_path) as f:
            self._data = json.load(f)

    def get(self, key, default=None):
        return self._data.get(key, default)
# usage:
# cfg = EnvConfig()
# cfg.get('base_url')
