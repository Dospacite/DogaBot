import json
from pathlib import Path


class RegistryHandler:
    registry_path: Path
    cached_registry: dict

    def __init__(self, registry_path: Path):
        self.registry_path = registry_path
        self.cached_registry = {}

    def dump_dict_to_registry(self, pairs: dict):
        with self.registry_path.open("w") as f:
            json.dump(pairs, f)
            self.cached_registry = pairs

    def load_dict_from_registry(self):
        if self.cached_registry:
            return self.cached_registry
        with self.registry_path.open("r") as f:
            pairs = json.load(f)
            self.cached_registry = pairs
            return pairs

    def set_key(self, key: str, value):
        pairs = self.load_dict_from_registry()
        pairs[key] = value
        self.dump_dict_to_registry(pairs)

    def get_key(self, key: str):
        pairs = self.load_dict_from_registry()
        return pairs[key]
