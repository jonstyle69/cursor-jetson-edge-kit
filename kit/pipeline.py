"""
Pipeline orchestration for combining camera and inference components.

Manages the flow: Camera → Inference → Results
Future: Will support async processing, multi-threading, and result visualization.
"""

from typing import Optional, Dict, Any
import numpy as np

from kit.camera import Camera
from kit.inference import InferenceEngine


class Pipeline:
    """
    Pipeline that orchestrates camera capture and inference.
    
    Combines Camera and InferenceEngine to create a complete Edge AI pipeline.
    Currently supports single-step execution (run_once).
    Future: Will support continuous loops, async processing, and result callbacks.
    
    Example:
        >>> camera = Camera(source="0")
        >>> engine = InferenceEngine(model_path="models/model.onnx")
        >>> pipeline = Pipeline(camera, engine)
        >>> results = pipeline.run_once()
    """
    
    def __init__(self, camera: Camera, inference_engine: InferenceEngine):
        """
        Initialize pipeline with camera and inference engine.
        
        Args:
            camera: Camera instance for frame capture.
            inference_engine: InferenceEngine instance for running inference.
        """
        self.camera = camera
        self.inference_engine = inference_engine
    
    def run_once(self) -> Optional[Dict[str, Any]]:
        """
        Execute a single pipeline step: capture frame → run inference → return results.
        
        Returns:
            Dictionary containing inference results, or None if capture failed.
            Structure: {
                "frame": numpy.ndarray,  # Original frame
                "detections": [...],     # Detection results from inference
                "num_detections": int,   # Number of detections
                ...
            }
        """
        # Open camera if not already open
        if not self.camera.is_opened:
            if not self.camera.open():
                print("Failed to open camera")
                return None
        
        # Capture frame
        success, frame = self.camera.read()
        if not success or frame is None:
            print("Failed to capture frame")
            return None
        
        # Run inference
        try:
            inference_results = self.inference_engine.infer(frame)
            
            # Combine frame and results
            return {
                "frame": frame,
                **inference_results
            }
        except Exception as e:
            print(f"Inference error: {e}")
            return None
    
    def cleanup(self) -> None:
        """
        Clean up resources (camera, inference engine).
        
        Call this when done with the pipeline.
        """
        self.camera.release()

