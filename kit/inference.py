"""
Inference abstraction.

In v0.1 this is a fake inference engine that returns a hard-coded
detection result. Later this will be replaced with real ONNX /
TensorRT / TFLite models.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List

import numpy as np


@dataclass
class InferenceEngine:
    """
    Minimal inference engine.

    Parameters
    ----------
    model_path:
        Placeholder path for a model. In the future this will point to
        an ONNX / TensorRT / other model file.
    """

    model_path: str

    def load(self) -> None:
        """
        Load the model into memory.

        In v0.1 this does nothing but exists as a hook for future versions.
        """
        # For future: load TensorRT engine / ONNX session here.
        print(f"[InferenceEngine] (v0.1) Pretending to load model from: {self.model_path}")

    def infer(self, frame: np.ndarray) -> List[Dict[str, Any]]:
        """
        Run inference on a single frame.

        Parameters
        ----------
        frame:
            Input image as a NumPy array (H, W, C).

        Returns
        -------
        List of detection dicts. Example:
        [
            {
                "label": "object",
                "score": 0.9,
                "bbox": [x1, y1, x2, y2],
            }
        ]
        """
        h, w, _ = frame.shape

        # Produce a single fake bounding box roughly in the center
        x1 = int(w * 0.3)
        y1 = int(h * 0.3)
        x2 = int(w * 0.7)
        y2 = int(h * 0.7)

        result = [
            {
                "label": "object",
                "score": 0.90,
                "bbox": [x1, y1, x2, y2],
            }
        ]
        return result
