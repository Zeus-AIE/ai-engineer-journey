# PowerShell Script khởi tạo môi trường ảo chuẩn kỹ thuật
Write-Host "🚀 Đang khởi tạo Virtual Environment (.venv)..." -ForegroundColor Cyan

# 1. Tạo môi trường ảo nếu chưa có
if (-not (Test-Path ".venv")) {
    python -m venv .venv
    Write-Host " Đã tạo thư mục .venv thành công." -ForegroundColor Green
} else {
    Write-Host "ℹ️ Thư mục .venv đã tồn tại." -ForegroundColor Yellow
}

# 2. Hướng dẫn kích hoạt
Write-Host "`n👉 Để kích hoạt môi trường ảo, hãy chạy lệnh sau:" -ForegroundColor White
Write-Host "   .\.venv\Scripts\Activate.ps1" -ForegroundColor Green

Write-Host "`n👉 Sau khi kích hoạt, cài đặt các gói bằng lệnh:" -ForegroundColor White
Write-Host "   pip install -r requirements.txt" -ForegroundColor Green
Write-Host "   python env_probe.py" -ForegroundColor Green
