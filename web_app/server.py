"""
AI Engineer Journey - Interactive Web Server & API
Zero-dependency HTTP server that serves the interactive roadmap dashboard and REST APIs.
"""
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import os
import platform
import shutil
import subprocess
import sys
import time
import urllib.parse

PORT = 8080
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")
PROGRESS_FILE = os.path.join(BASE_DIR, "progress.json")

# Ensure static directory exists
os.makedirs(STATIC_DIR, exist_ok=True)

ROADMAP_DATA = {
    "title": "AI Engineer Roadmap 2026 - Interactive Journey",
    "sources": [
        {"name": "Ch-Balaji/ai-engineer-roadmap", "url": "https://github.com/Ch-Balaji/ai-engineer-roadmap"},
        {"name": "mlabonne/llm-course", "url": "https://github.com/mlabonne/llm-course"},
        {"name": "roadmap.sh/ai-engineer", "url": "https://roadmap.sh/ai-engineer"},
        {"name": "Mì AI (miai.vn & thangnch)", "url": "https://miai.vn"}
    ],
    "phases": [
        {
            "id": 1,
            "code": "phase-1-foundation",
            "title": "Giai Đoạn 1: Chuẩn Hóa Môi Trường & Kỹ Thuật Nền (Foundations)",
            "badge": "Môi Trường & Hạ Tầng",
            "summary": "Làm chủ Linux headless, Docker Compose, Virtualenv, Git workflows và khai thác tăng tốc độ phần cứng qua CUDA.",
            "duration": "3-4 Tuần",
            "skills": ["Linux / VPS", "Docker & Compose", "Python Virtualenv", "PyTorch CUDA", "Git Architecture"],
            "labs": [
                {"id": "p1_lab1", "title": "Lab 1: Quét hệ thống phần cứng & Virtualenv (env_probe.py)", "completed": True},
                {"id": "p1_lab2", "title": "Lab 2: Đóng gói AI Microservice với Docker Hot-Reload", "completed": False},
                {"id": "p1_lab3", "title": "Lab 3: Cấu hình Headless Jupyter Server an toàn với SSH Tunneling", "completed": False},
                {"id": "p1_lab4", "title": "Lab 4: Chuẩn hóa cấu trúc thư mục dự án AI chuẩn Production", "completed": False}
            ]
        },
        {
            "id": 2,
            "code": "phase-2-machine-learning-cv",
            "title": "Giai Đoạn 2: Machine Learning & Computer Vision Thực Chiến",
            "badge": "Core ML & Vision",
            "summary": "Huấn luyện mô hình cơ bản, xử lý ảnh/video với OpenCV, Object Detection với YOLOv8/11 và đóng gói API.",
            "duration": "3-4 Tuần",
            "skills": ["Model Training Lifecycle", "OpenCV Video Stream", "YOLOv8/11 Inference", "FastAPI Endpoints"],
            "labs": [
                {"id": "p2_lab1", "title": "Lab 1: Huấn luyện và đánh giá mô hình ML cơ bản (Loss, Metrics)", "completed": False},
                {"id": "p2_lab2", "title": "Lab 2: Nhận diện vật thể thời gian thực với YOLO trên GPU RTX 3060", "completed": False},
                {"id": "p2_lab3", "title": "Lab 3: Xây dựng REST API phục vụ mô hình Computer Vision", "completed": False}
            ]
        },
        {
            "id": 3,
            "code": "phase-3-genai-rag-vectordb",
            "title": "Giai Đoạn 3: Kỷ Nguyên GenAI - LLM, Vector Database & RAG Chuyên Sâu",
            "badge": "Trọng Tâm Nghề Nghiệp",
            "summary": "Hiểu kiến trúc Transformer, bóc tách tài liệu với IBM Docling, Vector DB (Qdrant/Chroma), RAG code chay và Prompt Caching.",
            "duration": "5-6 Tuần",
            "skills": ["Transformer Architecture", "Document Parsing (Docling)", "Chunking Strategies", "Vector DB & Reranking", "Prompt Caching"],
            "labs": [
                {"id": "p3_lab1", "title": "Lab 1: Thử nghiệm trích xuất tài liệu phức tạp (PDF bảng biểu) với IBM Docling", "completed": False},
                {"id": "p3_lab2", "title": "Lab 2: Xây dựng hệ thống RAG 'code chay' Python kết hợp Vector Database", "completed": False},
                {"id": "p3_lab3", "title": "Lab 3: Tối ưu chi phí token và độ trễ với Prompt Caching", "completed": False},
                {"id": "p3_lab4", "title": "Lab 4: Fine-tune mô hình Embedding cho văn bản Tiếng Việt", "completed": False}
            ]
        },
        {
            "id": 4,
            "code": "phase-4-agentic-mcp-automation",
            "title": "Giai Đoạn 4: Agentic AI, Model Context Protocol (MCP) & Tự Động Hóa",
            "badge": "Agentic & Protocols",
            "summary": "Xây dựng Agent tự suy nghĩ và hành động với LangGraph, quản lý bộ nhớ dài hạn, tạo MCP Server và tự động hóa với n8n.",
            "duration": "4-5 Tuần",
            "skills": ["LangGraph StateGraph", "Memory Systems (Memori)", "Model Context Protocol (MCP)", "n8n AI Workflows"],
            "labs": [
                {"id": "p4_lab1", "title": "Lab 1: Xây dựng hệ thống Multi-Agent phân nhánh với LangGraph", "completed": False},
                {"id": "p4_lab2", "title": "Lab 2: Tự viết MCP Server trong 5 phút cấp quyền cho Claude/Cursor/Agent", "completed": False},
                {"id": "p4_lab3", "title": "Lab 3: Dựng luồng tự động hóa n8n tích hợp Gemini Node và Webhook", "completed": False}
            ]
        },
        {
            "id": 5,
            "code": "phase-5-production-security-mlops",
            "title": "Giai Đoạn 5: Production, Bảo Mật, Private AI Stack & MLOps",
            "badge": "Enterprise & MLOps",
            "summary": "Chạy mô hình nội bộ bằng Ollama/Open WebUI, Private AI Stack an toàn, chống Prompt Injection và đạo đức AI trong Ngân hàng.",
            "duration": "3-4 Tuần",
            "skills": ["Local SLM / Ollama", "Open WebUI", "Private AI Architecture", "Prompt Injection Defense", "Responsible & Ethical AI"],
            "labs": [
                {"id": "p5_lab1", "title": "Lab 1: Triển khai cụm Private AI Stack nội bộ (Ollama + Open WebUI)", "completed": False},
                {"id": "p5_lab2", "title": "Lab 2: Thiết lập Guardrails phòng thủ tấn công Prompt Injection & rò rỉ dữ liệu", "completed": False},
                {"id": "p5_lab3", "title": "Lab 3: Đóng gói đồ án Capstone hoàn chỉnh với Docker và CI/CD", "completed": False}
            ]
        }
    ]
}

def load_progress():
    if os.path.exists(PROGRESS_FILE):
        try:
            with open(PROGRESS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    # Default progress
    default_prog = {"p1_lab1": True}
    save_progress(default_prog)
    return default_prog

def save_progress(prog_data):
    with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
        json.dump(prog_data, f, ensure_ascii=False, indent=2)

def get_system_specs():
    cpu_count = os.cpu_count() or 1
    os_info = f"{platform.system()} {platform.release()}"
    python_ver = platform.python_version()
    
    # Check GPU
    gpu_info = "Không tìm thấy GPU NVIDIA"
    cuda_available = False
    nvidia_smi = shutil.which("nvidia-smi")
    if nvidia_smi:
        try:
            res = subprocess.run(["nvidia-smi", "--query-gpu=name,memory.total", "--format=csv,noheader"],
                                 capture_output=True, text=True, check=True)
            gpu_info = res.stdout.strip().replace("\n", ", ")
        except Exception:
            gpu_info = "NVIDIA Driver detected"

    try:
        import torch
        cuda_available = torch.cuda.is_available()
    except ImportError:
        pass

    return {
        "os": os_info,
        "python_version": python_ver,
        "cpu_cores": cpu_count,
        "gpu": gpu_info,
        "cuda_ready": cuda_available,
        "docker_installed": bool(shutil.which("docker")),
        "git_installed": bool(shutil.which("git")),
        "timestamp": time.time()
    }

class RoadmapHTTPHandler(BaseHTTPRequestHandler):
    def end_headers(self):
        # Allow cross-origin requests for local development
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        if path == "/api/roadmap":
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            
            # Merge saved progress into roadmap data
            prog = load_progress()
            data = json.loads(json.dumps(ROADMAP_DATA))
            for phase in data["phases"]:
                for lab in phase["labs"]:
                    lab["completed"] = bool(prog.get(lab["id"], False))
            self.wfile.write(json.dumps(data, ensure_ascii=False, indent=2).encode("utf-8"))
            return

        elif path == "/api/system":
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            specs = get_system_specs()
            self.wfile.write(json.dumps(specs, ensure_ascii=False, indent=2).encode("utf-8"))
            return

        elif path == "/api/progress":
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(json.dumps(load_progress(), ensure_ascii=False, indent=2).encode("utf-8"))
            return

        elif path == "/" or path == "/index.html":
            file_path = os.path.join(STATIC_DIR, "index.html")
            if os.path.exists(file_path):
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.end_headers()
                with open(file_path, "rb") as f:
                    self.wfile.write(f.read())
            else:
                self.send_error(404, "index.html not found")
            return

        else:
            # Static file serving
            rel_path = path.lstrip("/")
            target_path = os.path.normpath(os.path.join(STATIC_DIR, rel_path))
            if target_path.startswith(STATIC_DIR) and os.path.exists(target_path) and not os.path.isdir(target_path):
                self.send_response(200)
                mime = "text/plain"
                if target_path.endswith(".html"): mime = "text/html"
                elif target_path.endswith(".css"): mime = "text/css"
                elif target_path.endswith(".js"): mime = "application/javascript"
                elif target_path.endswith(".json"): mime = "application/json"
                elif target_path.endswith(".png"): mime = "image/png"
                elif target_path.endswith(".svg"): mime = "image/svg+xml"
                self.send_header("Content-Type", f"{mime}; charset=utf-8")
                self.end_headers()
                with open(target_path, "rb") as f:
                    self.wfile.write(f.read())
            else:
                self.send_error(404, f"Path not found: {path}")

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        if path == "/api/progress":
            content_length = int(self.headers.get("Content-Length", 0))
            post_data = self.rfile.read(content_length)
            try:
                payload = json.loads(post_data.decode("utf-8"))
                current = load_progress()
                current.update(payload)
                save_progress(current)
                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.end_headers()
                self.wfile.write(json.dumps({"success": True, "progress": current}).encode("utf-8"))
            except Exception as e:
                self.send_response(400)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.end_headers()
                self.wfile.write(json.dumps({"success": False, "error": str(e)}).encode("utf-8"))
            return
        else:
            self.send_error(404, "Endpoint not found")

    def log_message(self, format, *args):
        # Keep terminal log clean
        pass

def start_server(port=PORT):
    server_address = ("", port)
    httpd = HTTPServer(server_address, RoadmapHTTPHandler)
    print("=" * 65)
    print(f"🌟 AI Engineer Interactive Dashboard is running!")
    print(f"👉 Local URL: http://localhost:{port}")
    print(f"👉 API Endpoint: http://localhost:{port}/api/roadmap")
    print(f"👉 System Info: http://localhost:{port}/api/system")
    print("=" * 65)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Stopping server...")
        httpd.server_close()

if __name__ == "__main__":
    start_server()
