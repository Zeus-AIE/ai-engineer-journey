# Lab 05: Phân Tầng Bộ Nhớ Phần Cứng & CUDA Benchmark Profiler

> **Tiêu Chuẩn Học Thuật:** Stanford CS329S (Machine Learning Systems Design - Chip Huyen) & CMU 11-785 (Deep Learning Systems)  
> **Tiêu Chuẩn Kiến Trúc:** PSA (Production Software Architecture) & AI Systems 2026

## 1. Giới Thiệu
Bài thực hành này giúp AI Engineer hiểu rõ bản chất vật lý của tính toán Deep Learning:
* Tại sao **GPU Tensor Cores (FP16)** có thể tăng tốc độ nhân ma trận lên **70x+** so với CPU Intel/AMD.
* Cơ chế cấp phát bộ nhớ của PyTorch Caching Allocator (`allocated` vs `reserved` memory).
* Kỹ thuật giải phóng VRAM với `torch.cuda.empty_cache()` và chống tràn bộ nhớ CUDA Out-Of-Memory (OOM).
* Thiết lập chuẩn Production cho Docker (`--shm-size 8g`, non-root user).

## 2. Hướng Dẫn Thực Thi
```bash
python cuda_memory_benchmark.py
```

## 3. Kiến Thức Nền Tảng (Stanford CS329S & CMU 11-785)
* **GPU Memory Hierarchy:** Registers -> Shared Memory / L1 Cache -> L2 Cache -> VRAM GDDR6 -> Host RAM qua PCIe Bus.
* **PCIe Transfer Bottleneck:** Việc copy tensor giữa RAM và VRAM là điểm nghẽn lớn nhất. Sử dụng `pin_memory=True` và `non_blocking=True` trong PyTorch DataLoader để truyền dữ liệu bất đồng bộ.
* **Mixed Precision:** Chuyển đổi weights từ FP32 (32-bit float) sang FP16/BF16 giúp giảm một nửa dung lượng VRAM và kích hoạt trực tiếp các lõi Tensor Cores.
