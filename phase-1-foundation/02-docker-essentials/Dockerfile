# ==========================================================
# 🐳 Dockerfile Chuẩn Production cho AI Engineer
# ==========================================================

# 1. Chọn base image nhỏ gọn và bảo mật
FROM python:3.11-slim

# 2. Cài đặt các biến môi trường chuẩn Python
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# 3. Tạo thư mục làm việc trong container
WORKDIR /app

# 4. Tận dụng Docker Layer Cache: copy requirements trước
COPY requirements.txt .

# 5. Cài đặt các thư viện phụ thuộc
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copy toàn bộ mã nguồn vào container
COPY . .

# 7. Tạo user non-root để tăng cường bảo mật (Best Practice)
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

# 8. Mở cổng service
EXPOSE 8000

# 9. Lệnh chạy service
CMD ["python", "app.py"]
