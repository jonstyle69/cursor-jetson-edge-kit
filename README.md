# cursor-jetson-edge-kit

A beginner-friendly Edge AI development kit for building real-world NVIDIA Jetson demos using Cursor automation, modular pipelines, and practical SOPs.

## Vision

This kit solves the problem of helping half-career-switch engineers, PMs, and makers quickly build Edge AI demos using Cursor + Jetson. It provides a structured workflow that combines AI-powered code generation with hands-on hardware development, making Edge AI accessible to those without deep ML expertise.

## Who is this for?

- **Self-taught AI developers** who want to build practical Edge AI applications
- **Product Managers** who need hands-on experience with AI deployment
- **Makers** with a Jetson board looking for a structured development approach
- **Career switchers** transitioning into AI/ML engineering
- **Anyone** who wants to learn Edge AI development with modern tooling

## Features

### Planned / Roadmap

- 🎯 **Modular Pipeline Architecture**: Clean separation of camera, inference, and pipeline components
- 🤖 **Cursor-Powered Development**: Leverage AI assistance for rapid prototyping
- 📦 **Jetson-Optimized**: Ready-to-use modules for Jetson hardware (GStreamer, TensorRT)
- 🔧 **Beginner-Friendly**: Clear documentation and examples for each component
- 🚀 **Quick Start Templates**: Minimal examples to get you running in minutes
- 📚 **Comprehensive Docs**: Step-by-step guides from setup to deployment
- 🔒 **Security-First**: Built-in checks to prevent committing sensitive files

## Quick Start

### Prerequisites

- Python 3.10+
- NVIDIA Jetson device (for hardware deployment) or PC (for development)
- Cursor IDE (recommended) or any Python IDE

### Installation

```bash
# Clone the repository
git clone https://github.com/jonstyle69/cursor-jetson-edge-kit.git
cd cursor-jetson-edge-kit

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install the package
pip install -e .
```

### Run Your First Demo

```bash
# Run the minimal camera pipeline example
python examples/minimal_camera_pipeline.py
```

> **Note**: Currently, this example runs on PC with OpenCV. Jetson hardware support is coming soon.

## Repository Structure

```
cursor-jetson-edge-kit/
├── README.md                 # Project overview and quick start
├── LICENSE                   # MIT License
├── VERSION                   # Current version number
├── .gitignore                # Git ignore rules for Python/Jetson projects
├── .cursorrules              # Cursor IDE configuration and guidelines
│
├── docs/                     # Documentation
│   ├── 00_overview.md        # Project overview and vision
│   ├── 01_quickstart.md      # Getting started guide
│   ├── 02_jetson_setup.md    # Jetson hardware setup (TODO)
│   ├── 03_cursor_workflow.md # Cursor development workflow
│   └── 99_roadmap.md         # Project roadmap (TODO)
│
├── kit/                      # Core Python package
│   ├── __init__.py           # Package exports
│   ├── camera.py             # Camera interface (OpenCV/Jetson)
│   ├── inference.py          # Inference engine (TensorRT/ONNX/TFLite)
│   ├── pipeline.py           # Pipeline orchestration
│   └── config.py             # Configuration management
│
├── examples/                 # Example scripts
│   └── minimal_camera_pipeline.py  # Minimal working example
│
└── tools/                    # Development utilities
    └── git_semi_auto.sh      # Semi-automated Git workflow script
```

## Development Workflow

This project is designed to be developed with Cursor IDE. See `docs/03_cursor_workflow.md` for detailed workflow guidelines.

### Using the Git Semi-Auto Script

```bash
# Make the script executable (first time only)
chmod +x tools/git_semi_auto.sh

# Run the semi-automated Git workflow
bash tools/git_semi_auto.sh
```

This script helps you:
- Review changes before committing
- Check for sensitive files (models, .env, etc.)
- Create meaningful commit messages
- Push to remote safely

## License

MIT License

Copyright (c) 2025 JohnTao

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Contributing

Contributions are welcome! This project is designed to be a learning resource, so feel free to:
- Report issues
- Suggest improvements
- Submit pull requests
- Share your use cases

## Acknowledgments

Built for the community of makers, career switchers, and AI enthusiasts who want to bring Edge AI to life.

