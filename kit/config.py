"""
Configuration management for the Edge AI kit.

Provides default settings and configuration helpers.
Future: Will support YAML/JSON config files and environment variable overrides.
"""

import os


def get_default_camera_source() -> str:
    """
    Get the default camera source identifier.
    
    Returns:
        Default camera source (typically "0" for first USB webcam).
        Can be overridden via CAMERA_SOURCE environment variable.
    """
    return os.getenv("CAMERA_SOURCE", "0")


def get_default_model_path() -> str:
    """
    Get the default model path.
    
    Returns:
        Default model path.
        Can be overridden via MODEL_PATH environment variable.
    """
    return os.getenv("MODEL_PATH", "models/placeholder.onnx")


def get_inference_backend() -> str:
    """
    Get the preferred inference backend.
    
    Returns:
        Inference backend name ("tensorrt", "onnx", "tflite", or "placeholder").
        Can be overridden via INFERENCE_BACKEND environment variable.
    """
    return os.getenv("INFERENCE_BACKEND", "placeholder")

