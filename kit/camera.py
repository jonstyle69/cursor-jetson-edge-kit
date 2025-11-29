"""
Camera abstraction.

In v0.1 this uses OpenCV and is designed to work on a regular PC.
Later we can add Jetson / GStreamer / CSI camera backends.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Tuple

import cv2
import numpy as np


@dataclass
class Camera:
    """
    Simple camera wrapper.

    Parameters
    ----------
    source:
        OpenCV video source. Usually:
          - "0" (string) or 0 (int) for default webcam
          - a file path to a video
    """

    source: str = "0"
    _cap: Optional[cv2.VideoCapture] = None

    def open(self) -> None:
        """Open the camera if it is not already opened."""
        if self._cap is not None:
            return

        # Allow both "0" and 0
        src: int | str
        try:
            src = int(self.source)
        except ValueError:
            src = self.source

        self._cap = cv2.VideoCapture(src)
        if not self._cap.isOpened():
            # Fallback: create a dummy frame later
            self._cap.release()
            self._cap = None
            print("[Camera] Warning: failed to open camera, will use dummy frame.")

    def read(self) -> Tuple[bool, np.ndarray]:
        """
        Read a single frame.

        Returns
        -------
        success: bool
        frame: np.ndarray
            If camera cannot be opened, a dummy image is returned.
        """
        if self._cap is None:
            # Try to open once
            self.open()

        if self._cap is not None:
            ok, frame = self._cap.read()
            if ok:
                return True, frame
            print("[Camera] Warning: failed to read frame, falling back to dummy frame.")

        # Dummy 480x640 RGB frame (black)
        dummy = np.zeros((480, 640, 3), dtype=np.uint8)
        return True, dummy

    def release(self) -> None:
        """Release the underlying capture if opened."""
        if self._cap is not None:
            self._cap.release()
            self._cap = None
