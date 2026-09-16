# 👁️ Giai Đoạn 2: Machine Learning & Computer Vision Thực Chiến

> *"Trước khi bước vào thế giới LLM, một AI Engineer cần hiểu cặn kẽ cách huấn luyện mô hình, cách tính toán ma trận và cách xử lý luồng dữ liệu hình ảnh thời gian thực."* — Tư duy thực chiến từ **Mì AI**

---

## 🎯 Mục Tiêu Giai Đoạn 2
1. **Làm chủ vòng đời huấn luyện mô hình (ML Lifecycle):**
   * Hiểu rõ cách phân chia tập dữ liệu: Train (70%), Validation (15%), Test (15%).
   * Chẩn đoán hiện tượng học vẹt (Overfitting) và học chưa tới (Underfitting).
   * Đo lường chính xác với Precision, Recall, F1-Score, ROC-AUC.
2. **Computer Vision thời gian thực với YOLO:**
   * Tận dụng card đồ họa **NVIDIA GeForce RTX 3060 (CUDA 12.1)** trên máy bạn để chạy inference với tốc độ 60-100 FPS.
   * Hiểu cơ chế Bounding Box, Intersection over Union (IoU) và Non-Max Suppression (NMS).
3. **Đóng gói REST API với FastAPI:**
   * Đưa mô hình thị giác máy tính vào phục vụ người dùng qua HTTP endpoints chuẩn Production.

---

## 📂 Danh Sách Bài Thực Hành (Labs)
* **`01-ml-lifecycle/`**: Script huấn luyện, đánh giá ma trận nhầm lẫn (Confusion Matrix) và lưu trữ mô hình.
* **`02-yolo-inference/`**: Nhận diện vật thể thời gian thực qua webcam/video trên GPU RTX 3060.
* **`03-cv-fastapi-service/`**: API nhận diện ảnh trả kết quả JSON tọa độ vật thể bằng FastAPI.
