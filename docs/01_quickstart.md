# 01 – Quick Start  

Getting started in under 3 minutes.

---

## 1. Clone the repository

```bash
git clone https://github.com/jonstyle69/cursor-jetson-edge-kit.git
cd cursor-jetson-edge-kit
```

## 2. (Optional but recommended) Create a Python virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows (PowerShell):**

```bash
python -m venv .venv
.\.venv\Scripts\activate
```

## 3. Install dependencies

For now, we keep it lightweight.

```bash
pip install -e .
```

This enables local development mode and will automatically import modules under `kit/`.

## 4. Run the minimal example

This example:

- opens your webcam (if available)
- falls back to a dummy frame if unavailable
- runs fake inference
- prints detection results

```bash
python examples/minimal_camera_pipeline.py
```

**Expected output:**

```
[Example] Using camera source: 0
[Example] Using model path: models/fake_model.engine
[InferenceEngine] (v0.1) Pretending to load model...

[Example] Pipeline result:
  Frame shape : (480, 640, 3)
  Detections  :
    - label=object, score=0.90, bbox=[192, 144, 448, 336]

[Example] Done.
```

If you see this, the project is installed correctly.

## 5. Changing settings

This kit uses environment variables.

**Example:**

```bash
export CJEK_CAMERA_SOURCE=1
export CJEK_MODEL_PATH="models/my_model.engine"
```

Or create a `.env` file (NOT committed to Git):

```bash
CJEK_CAMERA_SOURCE=0
CJEK_MODEL_PATH=models/my_model.engine
```

## 6. Next steps

Once the minimal example works, you can:

- explore `kit/` to understand the pipeline
- try writing your own example script
- modify the fake inference into a real ONNX/TensorRT engine
- run everything on a Jetson board
- ask Cursor to generate more modules for you

---

## Troubleshooting

| Issue | Explanation | Fix |
|-------|-------------|-----|
| Camera fails to open | No webcam, wrong index | Set `CJEK_CAMERA_SOURCE` to a valid path |
| OpenCV not found | Missing dependency | `pip install opencv-python` |
| NumPy error | Version mismatch | `pip install numpy --upgrade` |
| Import error | Repo not installed | Run `pip install -e .` |

---

You are now ready to build your first Edge AI demo.
