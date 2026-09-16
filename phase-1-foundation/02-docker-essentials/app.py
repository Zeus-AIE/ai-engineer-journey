"""
Sample AI Microservice / Healthcheck API
Chạy dịch vụ HTTP nhẹ nhàng bằng Python Standard Library để kiểm chứng container
"""
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import os
import platform
import time

PORT = 8000

class SimpleAIServiceHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json; charset=utf-8")
        self.end_headers()

        response = {
            "status": "online",
            "service": "AI-Engineer-Foundation-Service",
            "timestamp": time.time(),
            "container_os": f"{platform.system()} {platform.release()}",
            "python_version": platform.python_version(),
            "working_directory": os.getcwd(),
            "message": " Chúc mừng bạn đã đóng gói và chạy thành công AI Service trong Docker container!",
            "miai_tip": "Khi đưa model AI vào Production, hãy đóng gói cả code và môi trường vào Docker để đảm bảo tính nhất quán trên mọi máy chủ."
        }
        self.wfile.write(json.dumps(response, ensure_ascii=False, indent=2).encode("utf-8"))

    def log_message(self, format, *args):
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {args[0]} - {args[1]}")

def run():
    server_address = ("", PORT)
    httpd = HTTPServer(server_address, SimpleAIServiceHandler)
    print("=" * 60)
    print(f"🚀 AI Service đang lắng nghe tại cổng http://0.0.0.0:{PORT}")
    print(f"👉 Mở trình duyệt và truy cập: http://localhost:{PORT}")
    print("=" * 60)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Đang dừng server...")
        httpd.server_close()

if __name__ == "__main__":
    run()
