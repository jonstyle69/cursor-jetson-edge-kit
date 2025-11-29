```
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║         cursor-jetson-edge-kit                               ║
║         Build Edge AI demos with Cursor + NVIDIA Jetson      ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
```

# cursor-jetson-edge-kit  

**A practical Edge AI starter kit combining Cursor automation + NVIDIA Jetson development.**  

Designed for self-taught engineers, PMs, and makers who want to build real-world AI demos—fast.

---

## 🚀 Vision

Modern AI development is changing.  
Cursor is becoming the new IDE.  
Jetson is becoming the default platform for edge deployment.  

Yet most beginners—especially career-switchers, PMs, and solo developers—struggle with:

- no structured guidance,  
- no reusable pipeline,  
- no clear SOP for Jetson development,  
- no safe Git workflow,  
- no examples that "just work,"  
- and no mentor who explains things in a practical way.

**cursor-jetson-edge-kit** solves this by giving you a simple, modular, beginner-friendly framework to bootstrap Edge AI projects with:

- clean folder structure  
- Cursor-friendly development workflow  
- Jetson-ready Python modules  
- minimal examples you can extend  
- opinionated SOP for how to actually build demos  

This is not another machine learning tutorial.  
This is a **real-world Edge AI development kit** for people who want to build **working demos** in days—not months.

---

## 🎯 Who is this for?

This kit is intentionally designed for:

- **Self-taught developers** entering AI/Edge computing  
- **PMs** who want real hands-on experience  
- **Makers & hobbyists** with Jetson Nano / Orin / Xavier  
- **Software engineers** new to Jetson or TensorRT  
- **Students** who need a structured mini-framework  
- **Career switchers** building their first portfolio project  

You do **not** need advanced AI/ML experience.  
If you can use Python and Cursor, you can ship a demo.

---

## ✨ Features (v0.1.0)

**Current:**

- Clean, production-ready project structure  
- Camera / Inference / Pipeline module skeleton  
- Minimal runnable example  
- Beginner-safe Git workflow (`tools/git_semi_auto.sh`)  
- MIT License (commercial-friendly)  
- Documentation starter files  
- Cursor development rules (`.cursorrules`)  

**Planned:**

- Jetson-optimized camera capture (GStreamer / CSI)  
- TensorRT inference module  
- Benchmark utilities  
- Multi-stage pipelines (preprocess → infer → postprocess)  
- Configurable YAML settings  
- Deployment scripts for Jetson  
- Video tutorials & walk-throughs  
- Example: YOLO + Jetson + Cursor full demo  
- Example: n8n Webhook pipeline  
- Example: OCR / barcode edge tools  

---

## 🧱 Project Structure

```text
cursor-jetson-edge-kit/

├─ README.md
├─ LICENSE
├─ VERSION
├─ .gitignore
├─ .cursorrules
│
├─ docs/
│  ├─ 00_overview.md
│  ├─ 01_quickstart.md
│  ├─ 02_jetson_setup.md
│  ├─ 03_cursor_workflow.md
│  └─ 99_roadmap.md
│
├─ kit/
│  ├─ __init__.py
│  ├─ camera.py
│  ├─ inference.py
│  ├─ pipeline.py
│  └─ config.py
│
├─ examples/
│  └─ minimal_camera_pipeline.py
│
└─ tools/
   └─ git_semi_auto.sh
```

---

## 📦 Quick Start

1. **Clone the repository**

```bash
git clone https://github.com/jonstyle69/cursor-jetson-edge-kit.git
cd cursor-jetson-edge-kit
```

2. **(Optional) Create a Python environment**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -e .
```

4. **Run the minimal example**

```bash
python examples/minimal_camera_pipeline.py
```

**Expected output (for now, fake inference):**

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

---

## 🔧 Core Concept: The Pipeline

This kit is built around a simple universal pattern for Edge AI demos:

```
Camera → Preprocess → Inference → Postprocess → Output
```

In v0.1 this looks like:

```
Pipeline.run_once()
│
├── camera.read()
├── inference.infer(frame)
└── return results
```

This simple design makes it easy to:

- swap camera backends
- replace models
- extend the pipeline
- deploy to Jetson
- automate development via Cursor

---

## 🧩 Minimal Example (Code Preview)

```python
from kit import Camera, InferenceEngine, Pipeline

camera = Camera()
engine = InferenceEngine("models/fake_model.engine")

pipeline = Pipeline(camera, engine)
result = pipeline.run_once()

print("Result:", result)
```

Super simple.  
Super extendable.  
Cursor can expand it automatically.

---

## 📚 Documentation

Documentation lives in the `docs/` directory.

**Recommended reading order:**

- `00_overview.md` – What this project is and why it exists
- `01_quickstart.md` – Start coding now
- `03_cursor_workflow.md` – How to use Cursor effectively
- `99_roadmap.md` – Future plans

---

## 🛡 License

MIT License

Copyright (c) 2025 JohnTao

This means:

- free for personal use
- free for commercial use
- no copyleft
- you keep full ownership of your commercial products

---

## 🗺 Roadmap (Short Version)

- [ ] Basic Jetson camera backend (GStreamer)
- [ ] TensorRT inference module
- [ ] Logging & monitoring
- [ ] Config system (YAML)
- [ ] Jetson deployment scripts
- [ ] Full real demo (YOLO + Jetson + Cursor)
- [ ] Video tutorials & documentation
- [ ] Community examples

---

## 💬 Contributing

Beginner-friendly pull requests are welcome.  
If you're using this kit for learning, feel free to open an issue describing your use case!

---

## ⭐ Why This Exists

To help thousands of beginners—career switchers, PMs, and self-learners—build Edge AI demos without feeling overwhelmed.

If Cursor is the new co-pilot,  
and Jetson is the new edge standard,  
this kit is the missing operating system between them.

---

---

# cursor-jetson-edge-kit（繁體中文版）

**實用的 Edge AI 開發工具包，結合 Cursor 自動化與 NVIDIA Jetson 開發。**

專為自學工程師、PM 和創客設計，幫助你快速建立真實世界的 AI 示範專案。

---

## 🚀 專案願景

現代 AI 開發正在改變。  
Cursor 正在成為新的 IDE。  
Jetson 正在成為邊緣部署的標準平台。  

然而，大多數初學者——特別是轉職者、PM 和獨立開發者——面臨以下困難：

- 缺乏結構化的指引  
- 沒有可重用的管道架構  
- 沒有清楚的 Jetson 開發 SOP  
- 沒有安全的 Git 工作流程  
- 沒有「開箱即用」的範例  
- 沒有以實務方式解釋的導師  

**cursor-jetson-edge-kit** 透過提供簡單、模組化、初學者友善的框架來解決這些問題，讓你能快速啟動 Edge AI 專案：

- 清晰的資料夾結構  
- 適合 Cursor 的開發工作流程  
- 可直接用於 Jetson 的 Python 模組  
- 可擴展的最小範例  
- 明確的 SOP，告訴你如何實際建立示範  

這不是另一個機器學習教學。  
這是為想要在**幾天內**——而非幾個月——建立**可運行的示範**的人準備的**真實世界 Edge AI 開發工具包**。

---

## 🎯 適合對象

這個工具包專為以下對象設計：

- **自學開發者**，剛進入 AI/Edge 運算領域  
- **PM**，想要實際動手體驗  
- **創客與愛好者**，擁有 Jetson Nano / Orin / Xavier  
- **軟體工程師**，剛接觸 Jetson 或 TensorRT  
- **學生**，需要結構化的小型框架  
- **轉職者**，正在建立第一個作品集專案  

你**不需要**高深的 AI/ML 經驗。  
只要會用 Python 和 Cursor，你就能產出一個示範。

---

## ✨ 功能特色 (v0.1.0)

**目前已有：**

- 乾淨、生產就緒的專案結構  
- 相機 / 推理 / 管道模組骨架  
- 最小可運行範例  
- 初學者安全的 Git 工作流程 (`tools/git_semi_auto.sh`)  
- MIT 授權（商業友善）  
- 文件起始檔案  
- Cursor 開發規則 (`.cursorrules`)  

**規劃中：**

- Jetson 優化的相機擷取 (GStreamer / CSI)  
- TensorRT 推理模組  
- 效能基準測試工具  
- 多階段管道 (前處理 → 推理 → 後處理)  
- 可配置的 YAML 設定  
- Jetson 部署腳本  
- 影片教學與逐步指南  
- 範例：YOLO + Jetson + Cursor 完整示範  
- 範例：n8n Webhook 管道  
- 範例：OCR / 條碼邊緣工具  

---

## 🧱 專案結構

```text
cursor-jetson-edge-kit/

├─ README.md
├─ LICENSE
├─ VERSION
├─ .gitignore
├─ .cursorrules
│
├─ docs/
│  ├─ 00_overview.md
│  ├─ 01_quickstart.md
│  ├─ 02_jetson_setup.md
│  ├─ 03_cursor_workflow.md
│  └─ 99_roadmap.md
│
├─ kit/
│  ├─ __init__.py
│  ├─ camera.py
│  ├─ inference.py
│  ├─ pipeline.py
│  └─ config.py
│
├─ examples/
│  └─ minimal_camera_pipeline.py
│
└─ tools/
   └─ git_semi_auto.sh
```

---

## 📦 快速開始

1. **複製專案**

```bash
git clone https://github.com/jonstyle69/cursor-jetson-edge-kit.git
cd cursor-jetson-edge-kit
```

2. **（建議）建立 Python 虛擬環境**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows (PowerShell):**

```bash
python -m venv .venv
.\.venv\Scripts\activate
```

3. **安裝依賴**

```bash
pip install -e .
```

4. **執行最小範例**

```bash
python examples/minimal_camera_pipeline.py
```

**預期輸出（目前為假推理結果）：**

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

---

## 🔧 核心概念：管道架構

這個工具包圍繞著 Edge AI 示範的簡單通用模式：

```
Camera → Preprocess → Inference → Postprocess → Output
```

在 v0.1 中，實作如下：

```
Pipeline.run_once()
│
├── camera.read()
├── inference.infer(frame)
└── return results
```

這個簡單的設計讓你可以輕鬆：

- 替換相機後端
- 更換模型
- 擴展管道
- 部署到 Jetson
- 透過 Cursor 自動化開發

---

## 🧩 最小範例（程式碼預覽）

```python
from kit import Camera, InferenceEngine, Pipeline

camera = Camera()
engine = InferenceEngine("models/fake_model.engine")

pipeline = Pipeline(camera, engine)
result = pipeline.run_once()

print("Result:", result)
```

超級簡單。  
超級可擴展。  
Cursor 可以自動擴展它。

---

## 📚 文件

文件位於 `docs/` 目錄。

**建議閱讀順序：**

- `00_overview.md` – 這個專案是什麼以及為什麼存在
- `01_quickstart.md` – 現在就開始寫程式
- `03_cursor_workflow.md` – 如何有效使用 Cursor
- `99_roadmap.md` – 未來計畫

---

## 🛡 授權

MIT License

Copyright (c) 2025 JohnTao

這表示：

- 個人使用免費
- 商業使用免費
- 無 copyleft
- 你完全擁有商業產品的所有權

---

## 🗺 路線圖（簡短版）

- [ ] 基礎 Jetson 相機後端 (GStreamer)
- [ ] TensorRT 推理模組
- [ ] 日誌與監控
- [ ] 設定系統 (YAML)
- [ ] Jetson 部署腳本
- [ ] 完整真實示範 (YOLO + Jetson + Cursor)
- [ ] 影片教學與文件
- [ ] 社群範例

---

## 💬 貢獻

歡迎初學者友善的 Pull Request。  
如果你正在使用這個工具包學習，歡迎開 issue 描述你的使用案例！

---

## ⭐ 為什麼存在

為了幫助數千名初學者——轉職者、PM 和自學者——建立 Edge AI 示範，而不感到不知所措。

如果 Cursor 是新的副駕駛，  
而 Jetson 是新的邊緣標準，  
這個工具包就是它們之間缺失的作業系統。
