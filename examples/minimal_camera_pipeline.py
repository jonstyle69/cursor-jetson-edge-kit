"""
Minimal camera pipeline example.

This example demonstrates the basic usage of the cursor-jetson-edge-kit:
1. Create a Camera instance
2. Create an InferenceEngine instance
3. Combine them in a Pipeline
4. Run inference and print results

This is a simple, beginner-friendly example that shows the core architecture.
"""

from kit import Camera, InferenceEngine, Pipeline
from kit.config import get_default_camera_source, get_default_model_path


def main():
    """Run a minimal camera pipeline example."""
    print("=" * 50)
    print("Minimal Camera Pipeline Example")
    print("=" * 50)
    print()
    
    # Step 1: Create camera instance
    camera_source = get_default_camera_source()
    print(f"[1/4] Creating camera with source: {camera_source}")
    camera = Camera(source=camera_source)
    
    # Step 2: Create inference engine
    model_path = get_default_model_path()
    print(f"[2/4] Creating inference engine with model: {model_path}")
    engine = InferenceEngine(model_path=model_path)
    print(f"[2/4] Loading model...")
    engine.load()
    
    # Step 3: Create pipeline
    print("[3/4] Creating pipeline (camera + inference)")
    pipeline = Pipeline(camera=camera, inference_engine=engine)
    
    # Step 4: Run inference
    print("[4/4] Running pipeline (capture frame → inference)")
    print()
    results = pipeline.run_once()
    
    if results is None:
        print("❌ Pipeline execution failed")
        return
    
    # Print results
    print("=" * 50)
    print("Inference Results:")
    print("=" * 50)
    print(f"Frame shape: {results.get('frame_shape', 'N/A')}")
    print(f"Number of detections: {results.get('num_detections', 0)}")
    
    detections = results.get('detections', [])
    if detections:
        print("\nDetections:")
        for i, det in enumerate(detections, 1):
            print(f"  Detection {i}:")
            print(f"    BBox: {det.get('bbox', 'N/A')}")
            print(f"    Score: {det.get('score', 'N/A'):.2f}")
            print(f"    Class: {det.get('class_name', 'N/A')}")
    else:
        print("\nNo detections found (this is expected with placeholder inference)")
    
    print()
    print("=" * 50)
    print("✅ Example completed successfully!")
    print("=" * 50)
    print()
    print("Note: This example uses placeholder inference.")
    print("In future versions, this will run real model inference.")
    
    # Cleanup
    pipeline.cleanup()


if __name__ == "__main__":
    main()

