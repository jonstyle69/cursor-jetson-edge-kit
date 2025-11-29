"""
High-level pipeline that connects Camera and InferenceEngine.

The goal is to keep this simple and extensible:
  Pipeline.run_once() → read frame → infer → return results
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List

import numpy as np

from .camera import Camera
from .inference import InferenceEngine


@dataclass
class Pipeline:
    """
    Simple one-step AI pipeline.

    It glues together:
      - a Camera (frame source)
      - an InferenceEngine (AI model)

    In the future we can extend this to support:
      - preprocessing
      - postprocessing
      - streaming loops
      - callbacks / hooks
    """

    camera: Camera
    engine: InferenceEngine

    def run_once(self) -> Dict[str, Any]:
        """
        Read one frame and run inference.

        Returns
        -------
        dict with:
          - "frame_shape": tuple
          - "detections": list of detection dicts
        """
        ok, frame = self.camera.read()
        if not ok:
            raise RuntimeError("Failed to read frame from camera.")

        if not isinstance(frame, np.ndarray):
            raise TypeError("Camera returned non-numpy frame.")

        detections: List[Dict[str, Any]] = self.engine.infer(frame)

        return {
            "frame_shape": frame.shape,
            "detections": detections,
        }
