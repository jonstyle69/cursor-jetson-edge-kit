"""
Camera interface for capturing frames from various sources.

Currently supports OpenCV-based camera access (USB webcam, built-in camera).
Future versions will support Jetson-specific sources (GStreamer, MIPI CSI).
"""

from typing import Optional
import cv2


class Camera:
    """
    Camera interface for frame capture.
    
    Supports USB webcams and built-in cameras via OpenCV.
    Future: Will support Jetson GStreamer pipelines and MIPI CSI cameras.
    
    Example:
        >>> camera = Camera(source="0")
        >>> camera.open()
        >>> frame = camera.read()
        >>> camera.release()
    """
    
    def __init__(self, source: str = "0"):
        """
        Initialize camera with a source identifier.
        
        Args:
            source: Camera source identifier. 
                   For USB webcams, typically "0", "1", etc.
                   Future: Will support GStreamer pipeline strings for Jetson.
        """
        self.source = source
        self.cap: Optional[cv2.VideoCapture] = None
        self.is_opened = False
    
    def open(self) -> bool:
        """
        Open the camera connection.
        
        Returns:
            True if camera opened successfully, False otherwise.
        """
        try:
            # Convert string source to int if it's a numeric string
            source_int = int(self.source) if self.source.isdigit() else self.source
            self.cap = cv2.VideoCapture(source_int)
            self.is_opened = self.cap.isOpened()
            return self.is_opened
        except Exception as e:
            print(f"Error opening camera {self.source}: {e}")
            self.is_opened = False
            return False
    
    def read(self) -> Optional[tuple[bool, Optional[any]]]:
        """
        Read a frame from the camera.
        
        Returns:
            Tuple of (success: bool, frame: numpy.ndarray or None).
            Returns (False, None) if camera is not opened or read fails.
        """
        if not self.is_opened or self.cap is None:
            return False, None
        
        try:
            ret, frame = self.cap.read()
            return ret, frame
        except Exception as e:
            print(f"Error reading frame: {e}")
            return False, None
    
    def release(self) -> None:
        """
        Release the camera resource.
        
        Should be called when done using the camera to free resources.
        """
        if self.cap is not None:
            self.cap.release()
            self.is_opened = False
            self.cap = None
    
    def __enter__(self):
        """Context manager entry."""
        self.open()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.release()

