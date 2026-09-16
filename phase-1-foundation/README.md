# 📘 Giai Đoạn 1: Chuẩn Hóa Môi Trường & Kỹ Năng Kỹ Thuật Nền (Foundations)

> *"Một AI Engineer giỏi không bắt đầu bằng việc import torch hay langchain, mà bắt đầu từ việc làm chủ môi trường thực thi, đóng gói phần mềm và quản lý mã nguồn."* — Tư duy thực chiến từ **Mì AI**

---

## 🎯 Mục Tiêu Của Giai Đoạn 1
1. **Hiểu và kiểm soát môi trường Python:** Tránh lỗi "dependency hell", xung đột phiên bản, làm chủ virtual environment (`venv`, `uv`, `conda`).
2. **Làm chủ Docker & Containerization:** Biết cách đóng gói AI API / Service, cấu hình `docker-compose` gắn volume để dữ liệu và model không bị mất khi container tắt.
3. **Môi trường làm việc từ xa (Remote / Headless Server):** Hiểu cách cấu hình Jupyter Notebook / Lab an toàn trên máy chủ từ xa / VPS (như bài chia sẻ trên Mì AI).
4. **Chuẩn hóa cấu trúc thư mục dự án AI:** Biết cách phân chia `data/`, `models/`, `src/`, `notebooks/` và cấu hình `.gitignore` chuẩn để không đẩy file hàng chục GB lên GitHub.

---

## 📚 4 Bài Học Thực Hành (Hands-on Labs)

### 📌 Bài 1: Quản lý Môi trường Python & Kiểm tra Phần cứng (`01-python-env/`)
* **Vấn đề thực tế:** Khi chạy mô hình AI, bạn cần biết máy mình có card GPU NVIDIA không? Có CUDA không? Đang chạy bao nhiêu RAM? Thư viện cài đặt có tương thích không?
* **Thực hành:**
  * Tạo môi trường ảo riêng biệt:
    ```powershell
    python -m venv .venv
    .\.venv\Scripts\Activate.ps1
    ```
  * Chạy file `env_probe.py` để quét toàn bộ thông số hệ thống (CPU, RAM, GPU, CUDA, Driver).

### 📌 Bài 2: Đóng gói Ứng dụng AI bằng Docker & Docker Compose (`02-docker-essentials/`)
* **Vấn đề thực tế:** Câu nói kinh điển của sinh viên: *"Code chạy trên máy em bình thường mà lên máy khác/server lại lỗi!"*. Docker sinh ra để giải quyết triệt để vấn đề này.
* **Thực hành:**
  * Xem file `Dockerfile`: Cài đặt base image `python:3.11-slim`, tạo user thường (non-root) để bảo mật, tối ưu cache layer khi cài `requirements.txt`.
  * Xem file `docker-compose.yml`: Kết nối container, cấu hình volume mount để code thay đổi là container cập nhật ngay (hot-reload).
  * Lệnh thực thi:
    ```powershell
    docker compose up --build
    ```
  * Truy cập `http://localhost:8000` để xem kết quả trả về từ service.

### 📌 Bài 3: Cấu hình Jupyter Lab An toàn trên VPS / Remote Server (`03-jupyter-remote/`)
* **Vấn đề thực tế:** Khi đi làm, bạn sẽ thường xuyên làm việc với máy chủ Linux trên Cloud (GCP, AWS) hoặc VPS cấu hình GPU. Bạn không có giao diện Windows để click chuột mà phải bật Jupyter chạy ngầm dưới dạng background daemon có mật khẩu và token.
* **Thực hành:**
  * Đọc file cấu hình `jupyter_server_config.py`.
  * Nắm được các tham số bảo mật quan trọng:
    * `c.ServerApp.ip = '0.0.0.0'` (lắng nghe mọi IP hoặc bind nội bộ).
    * `c.ServerApp.open_browser = False` (không cố gắng mở browser trên server không có GUI).
    * `c.ServerApp.password` (bắt buộc đặt mật khẩu băm, không để lộ Jupyter mở công khai).

### 📌 Bài 4: Chuẩn Hóa Cấu Trúc Dự Án AI (Production Project Template) (`04-standard-project-template/`)
* **Vấn đề thực tế:** Dự án AI thường chứa các file dữ liệu nặng (dataset .csv, .parquet, ảnh .jpg) và file checkpoint mô hình (.pt, .bin, .onnx, .safetensors) lên tới hàng GB. Đẩy nhầm lên Git sẽ làm hỏng repository.
* **Thực hành:**
  * Khảo sát cây thư mục chuẩn:
    ```
    my-ai-project/
    ├── data/
    │   ├── raw/            # Dữ liệu gốc bất biến
    │   └── processed/      # Dữ liệu sau khi làm sạch
    ├── models/             # File weights (chỉ lưu cục bộ hoặc dùng DVC)
    ├── notebooks/          # Thử nghiệm EDA, POC (sạch sẽ, có đánh số thứ tự)
    ├── src/
    │   ├── api/            # FastAPI / REST endpoints
    │   ├── core/           # Thuật toán chính / Pipeline RAG / Agent
    │   └── utils/          # Hàm trợ giúp, log, config
    ├── tests/              # Unit test và integration test
    ├── Dockerfile
    ├── docker-compose.yml
    ├── requirements.txt
    └── .gitignore          # Chặn triệt để file nặng và file môi trường (.venv)
    ```

---

## ✅ Checklist Hoàn Thành Giai Đoạn 1
- [ ] Đã kích hoạt môi trường ảo `.venv` thành công.
- [ ] Đã chạy `python 01-python-env/env_probe.py` và hiểu thông số đầu ra.
- [ ] Đã build và chạy thành công container với `docker compose up`.
- [ ] Hiểu rõ nguyên lý cấu hình server không đầu (Headless server) và cấu trúc thư mục dự án chuẩn.
