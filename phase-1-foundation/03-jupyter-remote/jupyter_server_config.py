# ==========================================================
# 📓 Cấu hình Jupyter Server Chạy Trên VPS/Server Từ Xa
# (Phỏng theo bài chia sẻ thực chiến trên Mì AI)
# ==========================================================

# 1. Cho phép truy cập từ mọi địa chỉ IP (hoặc giới hạn trong mạng nội bộ)
c.ServerApp.ip = '0.0.0.0'

# 2. Cổng mặc định
c.ServerApp.port = 8888

# 3. Không tự động bật trình duyệt (vì server/VPS thường không có màn hình GUI)
c.ServerApp.open_browser = False

# 4. Cho phép chạy dưới quyền root nếu đang ở trong Docker container
c.ServerApp.allow_root = True

# 5. Thư mục gốc khi mở Jupyter
c.ServerApp.root_dir = '/workspace'

# 6. BẢO MẬT: Bắt buộc đặt mật khẩu hoặc token để tránh bị scan quét trên Internet
# Sinh chuỗi băm mật khẩu bằng:
# python -c "from jupyter_server.auth import passwd; print(passwd('mat_khau_cua_ban'))"
# c.ServerApp.password = 'argon2:$argon2id$v=19$m=10240,t=10,p=8$...'
