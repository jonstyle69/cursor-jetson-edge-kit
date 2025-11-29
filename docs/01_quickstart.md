# Quick Start Guide

This guide will help you get `cursor-jetson-edge-kit` up and running on your machine.

## Prerequisites

- **Python 3.10+**: Check with `python --version`
- **Git**: For cloning the repository
- **Cursor IDE** (recommended) or any Python IDE
- **NVIDIA Jetson device** (optional for now - PC development is supported)

## Step 1: Clone the Repository

```bash
git clone https://github.com/jonstyle69/cursor-jetson-edge-kit.git
cd cursor-jetson-edge-kit
```

## Step 2: Create Virtual Environment

It's recommended to use a virtual environment to isolate dependencies:

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Linux/Mac:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

You should see `(venv)` in your terminal prompt when activated.

## Step 3: Install Dependencies

```bash
# Install the package in editable mode
pip install -e .
```

> **Note**: Currently, the package structure is minimal. As the project grows, a `setup.py` or `pyproject.toml` will be added with proper dependencies.

If you encounter any missing dependencies, you can install them manually:

```bash
pip install opencv-python numpy
```

## Step 4: Run Your First Example

Try running the minimal camera pipeline example:

```bash
python examples/minimal_camera_pipeline.py
```

This example:
- Creates a Camera instance (using OpenCV)
- Creates an InferenceEngine instance (with fake inference for now)
- Runs a single pipeline step
- Prints the inference results

> **Note**: Currently, this example runs on PC with OpenCV. Jetson hardware support and real model inference will be added in future updates.

## Step 5: Explore the Code

- Check `kit/` directory for the core modules
- Read `docs/03_cursor_workflow.md` to understand the development workflow
- Modify `examples/minimal_camera_pipeline.py` to experiment

## Troubleshooting

### Camera Issues

If you get camera errors:
- Make sure a camera is connected (USB webcam or built-in)
- On Linux, check camera permissions
- Try changing the camera source in the code (e.g., `"0"` to `"1"`)

### Import Errors

If you see import errors:
- Make sure the virtual environment is activated
- Run `pip install -e .` again
- Check that you're in the project root directory

### Jetson-Specific Setup

For Jetson hardware setup, see `docs/02_jetson_setup.md` (coming soon).

## Next Steps

- Read the [Overview](00_overview.md) to understand the project vision
- Learn about the [Cursor Workflow](03_cursor_workflow.md)
- Start building your own pipeline!

