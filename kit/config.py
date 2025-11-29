"""
Basic configuration helpers.

For now we keep things simple and read from environment variables
with safe defaults. Later this can be extended to YAML / TOML.
"""

from __future__ import annotations

import os
from typing import Optional


def get_env(key: str, default: Optional[str] = None) -> Optional[str]:
    """Read an environment variable with an optional default."""
    return os.getenv(key, default)


def get_default_camera_source() -> str:
    """
    Default camera source.

    On most systems:
      - "0" is the first webcam.
      - You can also pass a video file path.
    """
    return get_env("CJEK_CAMERA_SOURCE", "0")  # CJEK = cursor-jetson-edge-kit


def get_default_model_path() -> str:
    """
    Default model path.

    In v0.1 this is only used as a placeholder. Later we will plug in
    real ONNX / TensorRT models.
    """
    return get_env("CJEK_MODEL_PATH", "models/fake_model.engine")
