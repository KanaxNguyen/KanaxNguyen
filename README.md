<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f2027,50:203a43,100:2c5364&height=120&section=header" width="100%" alt=""/>

<h1 align="center">Nguyễn Nam Khánh</h1>

<p align="center">
  <b>AI Engineer (sinh viên)</b> · Computer Vision · LLM Agents & RAG · Full-stack · iOS
  <br/>
  <sub>FPT University Vietnam · VinUni AICB (AI Engineering, khóa K4)</sub>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white" alt="PyTorch"/>
  <img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white" alt="FastAPI"/>
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript"/>
  <img src="https://img.shields.io/badge/SwiftUI-F05138?style=flat-square&logo=swift&logoColor=white" alt="SwiftUI"/>
</p>

---

## 👋 Về mình

- 🎓 Sinh viên **FPT University Vietnam**, đang học chương trình **AI Engineering của VinUni AICB (K4)**.
- 🧠 Làm AI theo hướng **đưa vào sản phẩm**: từ dữ liệu, huấn luyện mô hình, đánh giá, đến backend, giao diện và ứng dụng di động.
- 🚗 Dự án chính hiện tại: **CabinSentinel**, hệ thống cảnh báo người hoặc thú cưng bị bỏ quên trong xe.
- 🔬 Quan tâm: Computer Vision, LLM Agents, RAG, đánh giá mô hình, độ tin cậy khi chạy production.
- 🧾 Thói quen: ghi rõ giới hạn của dự án (dữ liệu mô phỏng, demo học tập) ngay trong README.

## 🚀 Dự án nổi bật

### 🚗 CabinSentinel — cảnh báo trẻ em / thú cưng bị bỏ quên trong xe
Dự án nhóm. Mình phụ trách **backend an toàn** (nhận dữ liệu cảm biến qua MQTT và kết quả Vision qua HTTP, đánh giá rủi ro, vòng đời sự cố) và **ứng dụng di động**.
- [**CabinSentinel-mobile**](https://github.com/KanaxNguyen/CabinSentinel-mobile): app Expo / React Native + bản web, đăng nhập OTP, trạng thái xe, xử lý sự cố, đưa đón. Dữ liệu cũ hoặc mất kết nối **không bao giờ** hiển thị là “an toàn”.
- [**DepthLab**](https://github.com/KanaxNguyen/DepthLab): app SwiftUI đo thực nghiệm LiDAR và TrueDepth trên iPhone, xác định cảm biến nhìn xa và đáng tin tới đâu khi gắn gần gương chiếu hậu.

`FastAPI` `MQTT` `SQLite` `Docker` `YOLO` `Expo` `React Native` `SwiftUI` `ARKit`

### 🛣️ [Vietnam ADAS](https://github.com/KanaxNguyen/DAP_Project_ADAS_support) — biển báo tốc độ & phân vùng làn đường
Đồ án môn Phân tích dữ liệu (nhóm 6). Mô hình đa nhiệm tự xây từ đầu: backbone ResNet + FPN, đầu phát hiện kiểu YOLO, nhánh phân vùng đường; Focal / CIoU / Dice loss, suy luận cắt lát kiểu SAHI, bộ theo dõi IoU tự viết; suy ra tốc độ cho phép theo luật giao thông Việt Nam.

`PyTorch` `torchvision` `Computer Vision`

### 🚄 [HSR PyTorch MVP](https://github.com/KanaxNguyen/aiforinnovation) — AI cho đường sắt
Dự báo nhu cầu, dự báo hủy vé, tối ưu danh sách chờ theo chặng và đề xuất giá. Ba mô hình PyTorch (DemandNet, CancellationNet, PricePolicyNet), quy hoạch động cho waitlist, crawler lịch & giá công khai, dashboard Streamlit.

`PyTorch` `Streamlit` `Dynamic Programming` `Web crawling`

### 📅 [HUCE Teaching Assignment](https://github.com/KanaxNguyen/huce-teaching-assignment-mvp) — phân công giảng dạy tự động
Nhập lịch học từ Excel, chuẩn hóa dữ liệu, quản lý ràng buộc cứng/mềm, phát hiện lớp ghép và tự động phân công bằng **OR-Tools CP-SAT**; xuất thời khóa biểu theo giảng viên.

`Next.js` `TypeScript` `FastAPI` `SQLAlchemy` `OR-Tools`

### 🧑‍🏫 [Face Attendance Demo](https://github.com/KanaxNguyen/face-attendance-demo-public) — điểm danh bằng khuôn mặt
Hệ thống điểm danh phân quyền Admin / Giảng viên / Sinh viên. Pipeline MTCNN → căn chỉnh → FaceNet 512D → cosine similarity, xác nhận qua 3 khung hình liên tiếp; không lưu ảnh camera.

`Flask` `MTCNN` `FaceNet` `SQLite`

### 📊 [Datathon 2026 — B.F.E Alliance](https://github.com/KanaxNguyen/Datathon2026-BFE)
EDA và dự báo doanh thu 548 ngày. Mô hình chọn: XGBoost trên target log (R² ≈ 0.625, SMAPE ≈ 25.3%), kèm ước lượng COGS và cảnh báo ngày rủi ro biên lợi nhuận.

`pandas` `scikit-learn` `XGBoost`

### Dự án khác

| Dự án | Nội dung | Công nghệ |
|---|---|---|
| [SnapTask AI](https://github.com/KanaxNguyen/SnapTask) | Biến ảnh chụp màn hình (chat, email, thông báo) thành danh sách việc có ưu tiên và hạn chót, xuất Google Calendar | React, Vite, Tailwind, Gemini |
| [Pose Match Game](https://github.com/KanaxNguyen/Check_pose_game-) | Game bắt chước tư thế qua camera, so sánh 11 góc cơ thể, 5 vòng tăng dần độ khó; làm cho sự kiện FPTU AI Club | MediaPipe Pose, JavaScript |
| [Fuel E10](https://github.com/KanaxNguyen/Oil_Price_Crawl) | Thu thập và làm sạch 5.281 dòng giá nhiên liệu Việt Nam & Malaysia, phân tích bằng SQL | Crawling, SQLite, SQL Server |
| [Emotion Detector](https://github.com/KanaxNguyen/emotion-detector-final-project) | Phân tích cảm xúc văn bản tiếng Anh qua Flask | Watson NLP, Flask |

## 🧪 VinUni AICB — các lab AI Engineering (K4)

| Ngày | Chủ đề |
|---|---|
| [01](https://github.com/KanaxNguyen/K4-L3-Day1-AI-LLM-Foundation) | Làm quen LLM API, trợ lý hội thoại trên terminal |
| [11](https://github.com/KanaxNguyen/K4-L3-DAY11-NguyenNamKhanh-2A202602568-Guardrails-HITL-Responsible-AI) | Guardrails, Human-in-the-loop, Responsible AI (red team / blue team) |
| [12](https://github.com/KanaxNguyen/K4-L3A-DAY12-NguyenNamKhanh-2A202602568-CloudServicesAndDeployment) | Cloud services & deployment |
| [13](https://github.com/KanaxNguyen/K4-L3-DAY13-NguyenNamKhanh-2A202602568-Monitoring-LLMOps) | Monitoring & LLMOps: logging, tracing, dashboard, SLO |
| [14](https://github.com/KanaxNguyen/K4-L3A-DAY14-NguyenNamKhanh-2A202602568-AIEvaluation) | Đánh giá hệ thống RAG với golden dataset |
| [16](https://github.com/KanaxNguyen/K4-DAY16-Track3A-NguyenNamKhanh-2A202602568-AgentArena) | Agent Arena — thi đấu agent 120 phút |
| [17](https://github.com/KanaxNguyen/K4-DAY17-NguyenNamKhanh-2A202602568) | Memory cho AI agent: ngắn hạn và dài hạn |
| [18](https://github.com/KanaxNguyen/K4-Track3A-DAY18-NguyenNamKhanh-2A202602568-ProductionRAG) | Production RAG |
| [19](https://github.com/KanaxNguyen/K4-DAY19-NguyenNamKhanh-2A202602568) | Knowledge Graph: Flat RAG và GraphRAG |
| [20](https://github.com/KanaxNguyen/K4-DAY20-MULTIAGENTS-NguyenNamKhanh-2A202602568) | Multi-agent |
| [21](https://github.com/KanaxNguyen/Day21-Track3-NguyenNamKhanh-2A202602568-Finetuning-Lab) | Fine-tuning LoRA với regression gate |
| [22](https://github.com/KanaxNguyen/K4-DAY22-NguyenNamKhanh-2A202602568) | Alignment bằng DPO / ORPO |
| [23](https://github.com/KanaxNguyen/K4-L3A-DAY23-NguyenNamKhanh-2A202602568-AdvanceDeepAgents-Labs) | Advanced Deep Agents |
| [25](https://github.com/KanaxNguyen/Track3-Day25-2A202602568-NguyenNamKhanh) | Độ tin cậy cho agent: circuit breaker, cache, idempotency, error budget |
| [26](https://github.com/KanaxNguyen/K4-DAY26-NguyenNamKhanh-2A202602568) | MCP và Function Calling |
| [27](https://github.com/KanaxNguyen/K4-DAY27-NguyenNamKhanh-2A202602568) | Human-in-the-loop: confidence routing, interrupt/resume, audit |

## 🛠️ Công nghệ

<p align="center">
  <img src="https://skillicons.dev/icons?i=py,pytorch,sklearn,fastapi,flask,django,sqlite,docker&theme=dark" alt="Python, PyTorch, scikit-learn, FastAPI, Flask, Django, SQLite, Docker"/>
  <br/>
  <img src="https://skillicons.dev/icons?i=ts,js,react,nextjs,vite,tailwind,swift,git&theme=dark" alt="TypeScript, JavaScript, React, Next.js, Vite, Tailwind, Swift, Git"/>
</p>

| Mảng | Đã dùng trong dự án |
|---|---|
| **AI / ML** | PyTorch, torchvision, scikit-learn, XGBoost, YOLO, MediaPipe, MTCNN + FaceNet, OR-Tools |
| **LLM** | LLM API, Gemini, RAG, GraphRAG, agent memory, multi-agent, MCP, LoRA, DPO / ORPO, guardrails, evaluation |
| **Backend** | FastAPI, Flask, Django, Node.js / Express, SQLAlchemy, SQLite, SQL Server, MQTT |
| **Frontend & Mobile** | React, Next.js, Vite, Tailwind, Streamlit, Expo / React Native, SwiftUI, ARKit |
| **Hạ tầng** | Docker, Vercel, Hugging Face Spaces, Git |

## 📊 Thống kê

<p align="center">
  <img height="165" src="https://github-readme-stats.vercel.app/api?username=KanaxNguyen&show_icons=true&theme=tokyonight&hide_border=true&count_private=true" alt="GitHub stats"/>
  <img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=KanaxNguyen&layout=compact&theme=tokyonight&hide_border=true&langs_count=8" alt="Top languages"/>
</p>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:2c5364,100:0f2027&height=100&section=footer" width="100%" alt=""/>
