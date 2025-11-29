"""
cursor-jetson-edge-kit

A beginner-friendly Edge AI development kit for building real-world 
NVIDIA Jetson demos using Cursor automation, modular pipelines, and practical SOPs.
"""

from kit.camera import Camera
from kit.inference import InferenceEngine
from kit.pipeline import Pipeline

__version__ = "0.1.0"
__all__ = ["Camera", "InferenceEngine", "Pipeline"]

