# src/atlas/decorators.py

from atlas.registry import registry


def metric(cls):
    registry.register(cls)
    return cls