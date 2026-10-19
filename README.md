<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f2027,50:203a43,100:2c5364&height=120&section=header" width="100%" alt=""/>

<h1 align="center">Nguyễn Nam Khánh</h1>

<p align="center">
  <b>AI Undergraduate</b> · Computer Vision & Edge AI · Prototyping & Research
  <br/>
  <sub>FPT University Hanoi · B.Sc. IT (Artificial Intelligence) · Hanoi, Vietnam</sub>
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/nam-kh%C3%A1nh-nguy%E1%BB%85n-56968a3b8"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
  <a href="https://www.kaggle.com/asdhjasdjhka"><img src="https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white" alt="Kaggle"/></a>
</p>

---

## 👋 About me

I turn real problems into working prototypes, end to end: from an **IoT edge device, backend and iOS app** that detect children left in parked cars, to a **scheduling tool piloted by a university lecturer**. I combine computer vision and full-stack engineering with research and team leadership.

- 🎓 **FPT University Hanoi**, B.Sc. IT – Artificial Intelligence · GPA **3.5/4.0**
- 🏅 **Full Tuition Scholarship** (100%, entire degree) · **Outstanding Student Award**, Fall 2025
- 📄 Co-author, **AIRoSIP 2026** (accepted)
- 🧑‍💼 Head of Technical Committee, **Tech-Fest 2026** · Vice Head, Technical Committee, **FPTU AI Club**
- 🌏 Vietnamese (native) · English (CEFR B2) · Japanese (basic)

## 🚀 Selected projects

### 🚗 CabinSentinel — child & pet left-behind detection in vehicles
<sub>Sep 2026 – present · 4-member team · my role: backend, IoT edge, iOS app</sub>

- **FastAPI backend & safety-rule engine**: incident lifecycle, device commands, RBAC and audit; unlocking always needs human confirmation; **490+ pytest tests**.
- **"No detection ≠ empty seat"** rule: on simulated cabin video where YOLOv8 never saw the child, false "empty" reports dropped from **288/288 to 0/288** frames.
- **Raspberry Pi 5 IoT service**: camera capture with on-device face blurring, SHT31 temperature and LD2410C radar readers, metadata-only uplink — raw images never leave the car.
- **Native iOS app — [CabinSentinel-iOS](https://github.com/KanaxNguyen/CabinSentinel-iOS)**: SwiftUI with iOS 26 **Liquid Glass**, **Live Activities & Dynamic Island**, the iPhone itself as the in-car sensor (wide / ultra-wide camera, GPS, battery & thermal state) with on-device **Core ML + Vision** detection and face cover; OTP sign-in, staged alerts, remote climate, school trips.
- Also public: [CabinSentinel-mobile](https://github.com/KanaxNguyen/CabinSentinel-mobile) (Expo / React Native + web client) · [DepthLab](https://github.com/KanaxNguyen/DepthLab) (SwiftUI tool measuring how far iPhone LiDAR and TrueDepth can be trusted inside a cabin).

`FastAPI` `SwiftUI` `CoreML` `YOLOv8` `Raspberry Pi 5` `MQTT` `Docker`

### 📅 [HUCE Teaching Assignment System](https://github.com/KanaxNguyen/huce-teaching-assignment-mvp)
<sub>Jul 2026 – present</sub>

- MVP for a university Mathematics department: imports messy Excel schedules and auto-assigns lecturers with **OR-Tools CP-SAT** (no clashes, balanced workload).
- **Piloted with a Mathematics lecturer** and revised from their feedback; ambiguous preferences go to a review list instead of being guessed.

`Next.js` `TypeScript` `FastAPI` `SQLAlchemy` `OR-Tools`

### 🛣️ [Context-Aware ADAS Perception for Vietnamese Roads](https://github.com/KanaxNguyen/DAP_Project_ADAS_support)
<sub>Jan – Mar 2026 · team lead, course project</sub>

- Detects Vietnamese speed and residential-zone signs and segments lanes and hard dividers with a **ResNet-FPN multi-task network** and IoU tracking.
- Collected and labeled **300 local images**; designed a unit-tested rule engine that infers the speed limit under **Circular 38/2024**.

`PyTorch` `ResNet-FPN` `IoU Tracking`

### 🚙 [VinFast Vehicle Detection under a No-YOLO Constraint](https://www.kaggle.com/code/asdhjasdjhka/vinfast-detector-v3-1)
<sub>2026 · Kaggle notebook</sub>

- Faster R-CNN detector for VinFast vehicles reaching **mAP@0.5 = 0.9523** with TTA, WBF and false-positive filtering.

`PyTorch` `Faster R-CNN` `Albumentations`

### More projects

| Project | What it does | Stack |
|---|---|---|
| [Datathon 2026 — B.F.E Alliance](https://github.com/KanaxNguyen/Datathon2026-BFE) | **Top 50, VinUni-Datathon 2026** · revenue forecasting, R² 0.625 | XGBoost, pandas |
| [HSR PyTorch MVP](https://github.com/KanaxNguyen/aiforinnovation) | Railway demand & cancellation forecasting, waitlist optimisation, dynamic pricing | PyTorch, Streamlit |
| [Face Attendance Demo](https://github.com/KanaxNguyen/face-attendance-demo-public) | Role-based attendance with MTCNN + FaceNet, no camera frames stored | Flask, SQLite |
| [Pose Match Game](https://github.com/KanaxNguyen/Check_pose_game-) | Real-time pose-matching game built for an FPTU AI Club event | MediaPipe, JavaScript |
| [SnapTask AI](https://github.com/KanaxNguyen/SnapTask) | Turns screenshots of chats and emails into a prioritised to-do list | React, Gemini |
| [Fuel E10](https://github.com/KanaxNguyen/Oil_Price_Crawl) | Crawls and cleans 5,281 fuel-price records (Vietnam & Malaysia) for SQL analysis | Crawling, SQL |

## 📄 Research

**AI-Driven Market Traction Forecasting for Digital Creative Products: Evidence from Indie Games on Steam** (2026)
<br/>V. N. Anh, **N. N. Khanh**, L. H. T. Lam, D. V. Hieu · *Accepted, AIRoSIP 2026 (unpublished)*

- Owned data collection and pipeline design: merged 4 public sources into **5,997 games × 52 features**.
- XGBoost cut log RMSE by **15.1%** vs. Ridge; chronological validation showed random splits overstate R² (**0.70 vs. 0.45**).

## 🧑‍💼 Leadership & activities

- **Head of Technical Committee — Tech-Fest 2026: Tech Journey**, FPTU AI Club (Jul 2026 – present): lead the committee designing three tech games (IoT Block Scratch Racing, Generative AI, Computer Vision).
- **Vice Head, Technical Committee — FPTU AI Club** (present)
- **Volunteer Organizer — FANROC Robotics Competition** (2026)

## 🧪 AI20K coursework — LLM, RAG & agents labs (Cohort 4)

| Day | Topic |
|---|---|
| [01](https://github.com/KanaxNguyen/K4-L3-Day1-AI-LLM-Foundation) | LLM API basics |
| [11](https://github.com/KanaxNguyen/K4-L3-DAY11-NguyenNamKhanh-2A202602568-Guardrails-HITL-Responsible-AI) | Guardrails, human-in-the-loop, responsible AI (red / blue team) |
| [12](https://github.com/KanaxNguyen/K4-L3A-DAY12-NguyenNamKhanh-2A202602568-CloudServicesAndDeployment) | Cloud services & deployment |
| [13](https://github.com/KanaxNguyen/K4-L3-DAY13-NguyenNamKhanh-2A202602568-Monitoring-LLMOps) | Monitoring & LLMOps: logging, tracing, dashboards, SLOs |
| [14](https://github.com/KanaxNguyen/K4-L3A-DAY14-NguyenNamKhanh-2A202602568-AIEvaluation) | RAG evaluation with a golden dataset |
| [17](https://github.com/KanaxNguyen/K4-DAY17-NguyenNamKhanh-2A202602568) | Memory systems for AI agents |
| [18](https://github.com/KanaxNguyen/K4-Track3A-DAY18-NguyenNamKhanh-2A202602568-ProductionRAG) | Production RAG |
| [19](https://github.com/KanaxNguyen/K4-DAY19-NguyenNamKhanh-2A202602568) | Knowledge graphs: flat RAG vs. GraphRAG |
| [20](https://github.com/KanaxNguyen/K4-DAY20-MULTIAGENTS-NguyenNamKhanh-2A202602568) | Multi-agent systems |
| [21](https://github.com/KanaxNguyen/Day21-Track3-NguyenNamKhanh-2A202602568-Finetuning-Lab) | LoRA fine-tuning with a regression gate |
| [22](https://github.com/KanaxNguyen/K4-DAY22-NguyenNamKhanh-2A202602568) | DPO / ORPO alignment |
| [25](https://github.com/KanaxNguyen/Track3-Day25-2A202602568-NguyenNamKhanh) | Agent reliability: circuit breakers, caching, idempotency |
| [26](https://github.com/KanaxNguyen/K4-DAY26-NguyenNamKhanh-2A202602568) | MCP vs. function calling |
| [27](https://github.com/KanaxNguyen/K4-DAY27-NguyenNamKhanh-2A202602568) | Human-in-the-loop: confidence routing, interrupt / resume |

## 🛠️ Skills

<p align="center">
  <img src="https://skillicons.dev/icons?i=py,pytorch,opencv,sklearn,fastapi,swift,nextjs,docker,raspberrypi&theme=dark" alt="Python, PyTorch, OpenCV, scikit-learn, FastAPI, Swift, Next.js, Docker, Raspberry Pi"/>
</p>

| Area | Tools |
|---|---|
| **Computer Vision & Edge AI** | PyTorch, OpenCV, YOLOv8, Faster R-CNN, NCNN, CoreML, Raspberry Pi 5 (I2C / serial sensors) |
| **AI & Data** | scikit-learn, XGBoost, SQL, OR-Tools CP-SAT, RAG and LLM agents |
| **Engineering & Product** | Python, FastAPI, Swift / SwiftUI, Next.js, Docker, pytest, user feedback loops, MVP prototyping |

## 📊 GitHub stats

<p align="center">
  <img height="165" src="https://github-readme-stats.vercel.app/api?username=KanaxNguyen&show_icons=true&theme=tokyonight&hide_border=true&count_private=true" alt="GitHub stats"/>
  <img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=KanaxNguyen&layout=compact&theme=tokyonight&hide_border=true&langs_count=8" alt="Top languages"/>
</p>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:2c5364,100:0f2027&height=100&section=footer" width="100%" alt=""/>
