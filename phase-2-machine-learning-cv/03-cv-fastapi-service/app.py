"""
Lab 3: Computer Vision Serving API with FastAPI
Nhận diện ảnh qua HTTP và trả về kết quả JSON bounding box
"""
import io
import time
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from PIL import Image

app = FastAPI(
    title="Computer Vision Inference Service",
    description="FastAPI REST endpoint for YOLO Object Detection",
    version="1.0.0"
)

# Dummy / lightweight detection logic or YOLO integration
@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "cv-object-detection", "gpu": "RTX 3060 CUDA"}

@app.post("/predict")
async def predict_image(file: UploadFile = File(...)):
    start_time = time.time()
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File tải lên bắt buộc phải là định dạng hình ảnh!")

    image_bytes = await file.read()
    try:
        image = Image.open(io.BytesIO(image_bytes))
        width, height = image.size
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Không thể đọc file ảnh: {str(e)}")

    # Giả lập kết quả phát hiện vật thể (hoặc gọi model.predict(image))
    mock_detections = [
        {
            "class_id": 0,
            "label": "person",
            "confidence": 0.94,
            "bbox": {"x_min": 120, "y_min": 80, "x_max": 350, "y_max": 500}
        },
        {
            "class_id": 2,
            "label": "car",
            "confidence": 0.88,
            "bbox": {"x_min": 400, "y_min": 250, "x_max": 620, "y_max": 480}
        }
    ]

    elapsed = (time.time() - start_time) * 1000

    return JSONResponse(content={
        "filename": file.filename,
        "image_dimensions": {"width": width, "height": height},
        "inference_time_ms": round(elapsed, 2),
        "detections_count": len(mock_detections),
        "detections": mock_detections
    })

if __name__ == "__main__":
    import uvicorn
    print("🚀 Khởi chạy FastAPI Computer Vision Service tại http://localhost:8001")
    uvicorn.run(app, host="0.0.0.0", port=8001)
