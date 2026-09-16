# ⚡ Tự Động Hóa AI Với n8n & Docker Compose

Dựa trên bài chia sẻ của Chủ tiệm Mì về:
* *Cách cài đặt n8n qua Docker Compose*
* *Tích hợp Gemini Node trên n8n không cần cấu hình HTTP Node thủ công*
* *Kỹ thuật Scale-up n8n để chịu tải cao*

---

## 🚀 Hướng Dẫn Chạy Cụm n8n

1. Khởi động container:
   ```bash
   docker compose up -d
   ```
2. Mở trình duyệt truy cập: `http://localhost:5678`
   * Tài khoản mặc định: `admin`
   * Mật khẩu: `miai_secure_password`
3. Tạo workflow mới:
   * Thêm Node **Webhook** (nhận request từ ngoài).
   * Kéo Node **Google Gemini** (phân tích intent / trích xuất thông tin).
   * Kéo Node **Telegram** (gửi thông báo khi có việc gấp).
