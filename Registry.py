import pathlib
import json
from typing import Optional


class DotDict(dict):
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


class Registry(DotDict):

    registry_file: pathlib.Path
    cached_registry: Optional[DotDict]

    def __init__(self, registry_file: pathlib.Path):
        super().__init__()
        self.registry_file = registry_file
        self.cached_registry = None

    def load(self):
        if self.cached_registry:
            return self.cached_registry
        with self.registry_file.open(mode="r", encoding="utf-8") as f:
            pairs = DotDict(json.load(f))
        self.cached_registry = pairs
        return pairs

    def dump(self, pairs):
        with self.registry_file.open(mode="w", encoding="utf-8") as f:
            json.dump(pairs, f, indent=4)
        self.cached_registry = pairs
