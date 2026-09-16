# 🚀 AI Engineer Roadmap (2026 Edition) - Synthesis of Global & Practical AI

> **Được tổng hợp từ các kho lưu trữ hàng đầu thế giới & triết lý thực chiến:**
> * [Ch-Balaji/ai-engineer-roadmap](https://github.com/Ch-Balaji/ai-engineer-roadmap) *(26-week curriculum & project-based)*
> * [mlabonne/llm-course](https://github.com/mlabonne/llm-course) *(The definitive guide to LLMs, Quantization, Fine-tuning)*
> * [roadmap.sh/ai-engineer](https://roadmap.sh/ai-engineer) & [roadmap.sh/prompt-engineering](https://roadmap.sh/prompt-engineering) *(Industry-standard skill tree & security)*
> * [zckly/ai-engineer-roadmap](https://github.com/zckly/ai-engineer-roadmap) *(Full-stack AI app development)*
> * [Mì AI (miai.vn & github.com/thangnch)](https://miai.vn) *(Hands-on Docker-first, Agentic AI, MCP & Enterprise Banking AI)*

---

## 🧭 Cây Kỹ Năng Cốt Lõi Của AI Engineer (2026 Skill Tree)

Khác với Data Scientist (tập trung phân tích thống kê) hay ML Researcher (tập trung phát minh kiến trúc mô hình mới), **AI Engineer** là kỹ sư đưa AI vào ứng dụng thực tế.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                            AI ENGINEER 2026                                 │
├─────────────────┬─────────────────┬──────────────────────┬──────────────────┤
│ 1. Foundations  │ 2. Core GenAI   │ 3. Agentic & MCP     │ 4. Production    │
├─────────────────┼─────────────────┼──────────────────────┼──────────────────┤
│ • Python 3.11+  │ • Transformer   │ • LangGraph / State  │ • Docker / K8s   │
│ • Linux / VPS   │ • RAG & Chunking│ • Multi-Agent System │ • Local SLM/vLLM │
│ • Docker Compose│ • Docling / OCR │ • MCP Servers (Fast) │ • Ollama / WebUI │
│ • Git Workflows │ • Vector DBs    │ • Memory (Memori)    │ • Prompt Caching │
│ • PyTorch & CUDA│ • Re-ranking    │ • n8n AI Automation  │ • Red Teaming    │
└─────────────────┴─────────────────┴──────────────────────┴──────────────────┘
```

---

## 📑 5 Giai Đoạn Học Tập Thực Chiến

### 📍 Giai Đoạn 1: Chuẩn Hóa Môi Trường & Kỹ Thuật Nền (Foundations)
* **Kiến thức:** Linux headless, Docker, Docker Compose, Virtualenv (`venv`/`uv`), Git workflow, PyTorch CUDA GPU acceleration.
* **Thực hành:**
  * Script quét phần cứng `env_probe.py`.
  * Đóng gói AI microservice với Docker & hot-reload.
  * Cấu hình SSH Tunneling bảo vệ Jupyter Server từ xa.
* **Thư mục code:** `phase-1-foundation/`

### 📍 Giai Đoạn 2: Machine Learning & Computer Vision Thực Chiến (ML & CV)
* **Kiến thức:** Huấn luyện mô hình, Data Pipeline, Convolutional Neural Networks, Object Detection (YOLOv8/11), OpenCV stream.
* **Thực hành:**
  * Xây dựng API phát hiện vật thể thời gian thực qua Webcam với FastAPI.
  * Đóng gói model weights và benchmark FPS trên GPU RTX 3060.
* **Thư mục code:** `phase-2-machine-learning-cv/`

### 📍 Giai Đoạn 3: Kỷ Nguyên GenAI – LLM, RAG & Vector Database (Advanced RAG)
* **Kiến thức:** Attention Mechanism, Tokenization, Document Parsing với **IBM Docling**, Chunking strategies, Embedding Models (Gemma Embedding, PhoBERT), Vector DB (Qdrant, Milvus, Chroma), Hybrid Search & Re-ranking.
* **Thực hành:**
  * RAG "Code chay" Python thuần (hiểu từng bước vector search & context injection).
  * Fine-tune mô hình Embedding cho dữ liệu tiếng Việt.
  * Áp dụng Prompt Caching để giảm 80% chi phí token API.
* **Thư mục code:** `phase-3-genai-rag-vectordb/`

### 📍 Giai Đoạn 4: Agentic AI, Model Context Protocol (MCP) & Tự Động Hóa
* **Kiến thức:** ReAct framework, LangGraph StateGraph, Tool Calling, Quản lý bộ nhớ trò chuyện (Memori), Chuẩn **Model Context Protocol (MCP)** của Anthropic, Tự động hóa với **n8n**.
* **Thực hành:**
  * Xây dựng Agent hỗ trợ tra cứu nội bộ tự biết dùng công cụ tìm kiếm và truy vấn SQL.
  * Tự viết MCP Server (bằng Storm MCP / FastMCP) để LLM đọc file hệ thống an toàn.
  * Tích hợp workflow tự động gửi thông báo qua Telegram khi Agent hoàn thành nhiệm vụ.
* **Thư mục code:** `phase-4-agentic-mcp-automation/`

### 📍 Giai Đoạn 5: Production, Bảo Mật, Private AI Stack & MLOps
* **Kiến thức:** Chạy Local LLM với Ollama / vLLM, Open WebUI frontend, Private AI Stack cho Doanh nghiệp, Phòng chống Prompt Injection / Jailbreaking, Đạo đức AI & Explainable AI (XAI) trong Ngân hàng.
* **Thực hành:**
  * Triển khai cụm Local AI Stack (Ollama + Open WebUI + Vector DB) bằng Docker Compose.
  * Thiết lập Guardrails kiểm duyệt đầu vào chống rò rỉ dữ liệu (Data Leakage).
* **Thư mục code:** `phase-5-production-security-mlops/`

---

## 🌐 Ứng Dụng Web Tương Tác Của Repo (Interactive Web App)

Dự án đi kèm một ứng dụng Web Dashboard trực quan giúp bạn:
1. Theo dõi tiến độ học tập theo từng tuần/giai đoạn.
2. Kiểm tra trực tiếp phần cứng và trạng thái môi trường máy tính (CPU/GPU/CUDA/Docker).
3. Đánh dấu checklist các bài thực hành đã hoàn thành.

👉 **Khởi động ứng dụng web:**
```bash
python web_app/server.py
```
Sau đó mở trình duyệt tại: **`http://localhost:8080`**
