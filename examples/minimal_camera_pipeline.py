"""
Minimal example: run a single-step pipeline.

This script is intentionally simple so that beginners can understand:
  - how Camera, InferenceEngine, and Pipeline are wired together
  - how to extend the kit for their own demos
"""

from __future__ import annotations

from kit import Camera, InferenceEngine, Pipeline
from kit.config import get_default_camera_source, get_default_model_path


def main() -> None:
    # 1. Build core components
    camera_source = get_default_camera_source()
    model_path = get_default_model_path()

    print(f"[Example] Using camera source: {camera_source}")
    print(f"[Example] Using model path:   {model_path}")

    camera = Camera(source=camera_source)
    engine = InferenceEngine(model_path=model_path)
    engine.load()

    pipeline = Pipeline(camera=camera, engine=engine)

    # 2. Run one step through the pipeline
    result = pipeline.run_once()

    print("\n[Example] Pipeline result:")
    print(f"  Frame shape : {result['frame_shape']}")
    print(f"  Detections  :")
    for det in result["detections"]:
        print(f"    - label={det['label']}, score={det['score']:.2f}, bbox={det['bbox']}")

    # 3. Clean up resources
    camera.release()
    print("\n[Example] Done.")


if __name__ == "__main__":
    main()
