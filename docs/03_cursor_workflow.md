# 03 – Cursor Development Workflow  

How to use Cursor effectively with this repository.

---

## Why a workflow?

Cursor is extremely powerful, but without structure:

- it may modify too many files at once  
- it may misunderstand your intentions  
- it may create breaking changes  
- it may introduce security issues  

To prevent that, this repository includes **.cursorrules** which defines clear rules.

This document explains the recommended workflow.

---

## 1. "Jetson Read" – Always read before coding

Before you ask Cursor to write code:

1. Show Cursor the existing file  
2. Ask it to summarize the current behavior  
3. Confirm the problem or objective  
4. Only then let Cursor propose code  

**Example prompt:**

```text
Read kit/inference.py.
Summarize what the current fake inference engine does.
I want to replace it with ONNX inference.
What files need to be changed?
```

Cursor will now work with context rather than hallucinating.

---

## 2. Use "Plan Before Code"

Every time you ask Cursor to modify multiple files, use this structure:

```text
PLAN:
- List which files to change
- Describe what will be changed
- Explain the high-level logic
Then implement the plan.
```

**Example:**

```text
Plan changes for adding TensorRT:
- kit/inference.py
  - add new TensorRTInferenceEngine
  - keep FakeInferenceEngine for compatibility
- examples/
  - new example file using TensorRT engine
- docs/
  - update 00_overview.md with new engine type

Proceed only after confirming the plan.
```

This prevents chaotic file edits.

---

## 3. Use the Git safety script

Never let Cursor run `git add`, `git commit`, or `git push`.

Instead, after Cursor finishes a batch of edits, run:

```bash
bash tools/git_semi_auto.sh
```

This script will:

- show what changed
- check for sensitive files
- prevent `.env`, `models`, `datasets`, `.engine`, `.onnx` from being committed
- ask for your commit message
- optionally push for you

This ensures your repo stays clean and safe.

---

## 4. Iteration loop (recommended)

Use this loop:

```text
Define task → Plan → Implement → Test locally → Record notes → Commit
```

For example:

1. "Add preprocessing to pipeline"
2. Cursor creates a plan
3. Cursor edits files
4. You run the example
5. If good → commit
6. If not → ask Cursor to fix specific errors

Keep the iterations small.  
Large multi-file changes should be avoided unless necessary.

---

## 5. How to request new modules from Cursor

**Example prompt:**

```text
Create a new module: kit/visualize.py  
It should draw bounding boxes using OpenCV.  
Provide a plan before coding.
```

Cursor will:

- propose a file
- generate a plan
- create minimal implementation
- update imports if needed

The `.cursorrules` ensures it does so cleanly.

---

## 6. When working on Jetson-specific features

Use prompts like:

```text
Add a new camera backend using GStreamer.  
Do not break PC compatibility.  
Use feature detection or environment variables.
```

Cursor will produce dual-path code with fallbacks.

---

## 7. When refactoring

Say:

```text
Refactor kit/pipeline.py for readability.  
Do not change the public API.  
Provide a detailed plan first.
```

Cursor will:

- keep existing class names
- keep imports working
- reorganize code safely

---

## 8. When documenting changes

Every time Cursor completes an iteration, ask:

```text
Summarize what changed in this iteration.
```

Copy that output into a personal dev log or Git commit message.

---

## Summary

Cursor is a powerful partner, but only when given structure.

This repository provides:

- `.cursorrules`
- clear folder structure
- explicit prompts
- beginner-safe pipeline
- Jetson-friendly abstractions

Follow this workflow and you will build strong, maintainable Edge AI demos—fast.
