# 🌐 Cấu Hình & Bảo Mật Jupyter Notebook Trên VPS Từ Xa

> **Bài học thực chiến từ Mì AI:** *"Nếu bạn mở Jupyter port 8888 ra ngoài Internet mà không đặt mật khẩu, hacker chỉ mất 10 giây để chiếm toàn quyền điều khiển (RCE - Remote Code Execution) trên server của bạn."*

---

## 🔒 3 Nguyên Tắc Bảo Mật Sống Còn Khi Triển Khai Jupyter Remote

1. **Luôn Băm Mật Khẩu (Hashed Password):**
   * Không lưu mật khẩu dạng bản rõ (plaintext).
   * Dùng lệnh băm chuẩn Argon2:
     ```bash
     python -c "from jupyter_server.auth import passwd; print(passwd('mat_khau_cua_ban'))"
     ```
   * Dán chuỗi băm vào `jupyter_server_config.py`.

2. **Sử dụng SSH Tunneling (Khuyên dùng nhất):**
   * Thay vì mở cổng `8888` trên tường lửa (UFW) của VPS, chỉ cho Jupyter lắng nghe ở `127.0.0.1`.
   * Trên máy tính cá nhân của bạn, tạo đường hầm SSH:
     ```bash
     ssh -N -f -L 8888:localhost:8888 user@dia_chi_ip_vps
     ```
   * Mở trình duyệt máy cá nhân và gõ: `http://localhost:8888`. Mọi dữ liệu truyền đi đều được mã hóa bằng giao thức SSH an toàn tuyệt đối.

3. **Chạy ngầm với Systemd hoặc Docker:**
   * Không chạy lệnh `jupyter notebook` trực tiếp trên cửa sổ terminal vì khi tắt kết nối SSH thì server cũng dừng theo.
   * Hãy đóng gói vào Docker hoặc tạo file service `systemd` để tự khởi động lại khi máy chủ reboot.
