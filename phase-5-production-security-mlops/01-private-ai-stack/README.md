# 🏢 Triển Khai Private AI Stack An Toàn Cho Doanh Nghiệp

Mô hình này giúp toàn bộ dữ liệu nội bộ không bao giờ rời khỏi mạng nội bộ (On-Premises / Private Cloud).

---

## 🚀 Hướng Dẫn Chạy Cụm Private AI

1. Khởi động các container:
   ```bash
   docker compose up -d
   ```
2. Tải mô hình nhỏ gọn chạy mượt trên GPU RTX 3060:
   ```bash
   docker exec -it local_ollama_engine ollama run qwen2.5:3b
   ```
3. Mở trình duyệt truy cập giao diện chat:
   👉 **`http://localhost:3000`**
   * Đăng ký tài khoản Admin nội bộ đầu tiên.
   * Chọn model `qwen2.5:3b` và trò chuyện với tốc độ cực cao trên GPU nội bộ.
