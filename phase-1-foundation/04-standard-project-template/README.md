# 📦 Standard AI Engineering Project Template

Cấu trúc thư mục này được thiết kế theo tiêu chuẩn công nghiệp (Production-ready), tương tự kiến trúc các repo thực chiến trên Mì AI và các công ty công nghệ lớn:

```
├── data/
│   ├── raw/            <- Dữ liệu gốc (read-only, không bao giờ chỉnh sửa trực tiếp)
│   └── processed/      <- Dữ liệu sạch sẵn sàng để train hoặc đưa vào Vector DB
├── models/             <- Nơi lưu trữ weights sau khi train (được ignore trên Git)
├── notebooks/          <- File Jupyter (.ipynb) để làm EDA, thử nghiệm nhanh
├── src/
│   ├── api/            <- REST API (FastAPI / Flask) phục vụ model
│   ├── core/           <- Pipeline chính (DataLoader, Model, RAG, Agent)
│   └── utils/          <- Logger, Config loader, Metric calculation
├── tests/              <- Unit test & Integration test
├── .dockerignore       <- Bỏ qua file rác khi build image
├── .gitignore          <- Chặn push file dung lượng lớn và file secret
├── Dockerfile          <- Đóng gói môi trường chạy chuẩn
├── docker-compose.yml  <- Điều phối các container (App, DB, Vector DB)
└── requirements.txt    <- Danh sách thư viện cần thiết
```

### 💡 Quy tắc vàng:
1. **Dữ liệu và Model Weights không bao giờ được commit trực tiếp vào Git.** Hãy dùng DVC (Data Version Control), lưu trữ trên S3/GCS hoặc tải tự động qua script.
2. **Notebooks chỉ dùng cho nghiên cứu thử nghiệm ban đầu (POC).** Khi đưa vào sản phẩm, toàn bộ code phải được chuyển đổi thành các module sạch trong thư mục `src/`.
