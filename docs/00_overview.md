# 00 – Overview

## What is cursor-jetson-edge-kit?

**cursor-jetson-edge-kit** is a beginner-friendly Edge AI development starter kit that combines:

- **Cursor** – AI-assisted IDE for rapid development  
- **NVIDIA Jetson** – the most common hardware platform for edge AI  
- **A clean SOP & modular pipeline** – so beginners can build real demos quickly  

This project is intentionally simple, well-structured, and predictable.  
It serves as a **real-world template** for building camera-based AI demos on both:

- regular PCs (development phase), and  
- Jetson devices (deployment phase).  

Whether your goal is learning, rapid prototyping, portfolio building, or teaching others, this kit offers a clean foundation.

---

## Why does this project exist?

Most beginners struggle with:

- too many scattered tutorials  
- no standard folder structure  
- unclear development workflow  
- no safe Git practice  
- difficulty connecting camera → inference → pipeline  
- being overwhelmed by Jetson setup  

And for career switchers or PMs learning Edge AI:

> "I don't know where to start,  
> I don't know what sequence to follow,  
> and I don't know how to make something that actually runs."

This kit fixes that with:

✔ A minimal pipeline  
✔ A step-by-step workflow  
✔ A reproducible project blueprint  
✔ Cursor automation for coding  
✔ Jetson-ready structure  
✔ Example scripts you can extend  

---

## High-level architecture

```text
cursor-jetson-edge-kit
│
├── kit/ → core modules
│ ├── camera.py → frame source
│ ├── inference.py → fake (later: TensorRT / ONNX)
│ ├── pipeline.py → glue logic
│ └── config.py → env/config helpers
│
├── examples/ → small runnable scripts
│ └── minimal_camera_pipeline.py
│
└── docs/ → how to use the kit
```

And the main processing flow:

```text
Camera → Preprocess → Inference → Postprocess → Result
```

In v0.1 we implement a simplified version:

```text
Pipeline.run_once()
├── Camera.read()
├── InferenceEngine.infer()
└── returns detections
```

---

## Who is this for?

This project is built for:

- self-taught developers  
- PMs who want hands-on AI skills  
- career switchers entering AI/Edge  
- makers and students  
- Jetson beginners who want structure  
- anyone learning how to use Cursor + AI coding  

You do NOT need advanced ML knowledge.

---

## What can you build with this?

Within the next versions (v0.1 → v0.4), you will be able to quickly build:

- image classification demos  
- object detection demos (ONNX/TensorRT)  
- barcode / QR code readers  
- edge OCR tools  
- offline kiosk-style applications  
- Jetson hardware camera demos  
- rapid prototypes for presentations  

This kit is designed to scale with your skills.

---

## Roadmap (Short Summary)

- Jetson GStreamer camera  
- Real ONNX/TensorRT inference  
- Configurable YAML settings  
- Demo loop (`run_forever`)  
- Visualization utilities  
- Example: YOLO inference  
- Example: simple offline kiosk  
- Example: AI sensor pipeline  

---

If you want to understand **why this kit matters**:  
You are holding the blueprint for how the next generation of developers will learn Edge AI.
