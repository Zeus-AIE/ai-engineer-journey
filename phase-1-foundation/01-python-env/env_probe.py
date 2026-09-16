"""
System & Hardware Environment Probe for AI Engineers
Kiểm tra cấu hình môi trường, phần cứng (CPU, RAM, GPU/CUDA) và virtualenv.
"""
import sys
import os
import platform
import subprocess
import shutil

# Ensure UTF-8 output encoding on Windows consoles
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def format_size(bytes_val):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes_val < 1024.0:
            return f"{bytes_val:.2f} {unit}"
        bytes_val /= 1024.0
    return f"{bytes_val:.2f} PB"

def check_system():
    print("=" * 60)
    print("[1] HE DIEU HANH & MOI TRUONG PYTHON")
    print("=" * 60)
    print(f"* He dieu hanh    : {platform.system()} {platform.release()} ({platform.architecture()[0]})")
    print(f"* Phien ban Python: {platform.python_version()} ({sys.executable})")
    
    # Check if running in a virtualenv
    in_venv = sys.prefix != sys.base_prefix
    status_venv = "[OK] Dang chay trong Virtualenv" if in_venv else "[!] Chua kich hoat Virtualenv (dang dung Python toan cuc)"
    print(f"* Trang thai Venv : {status_venv}")
    print(f"* Thu muc goc sys : {sys.prefix}")

def check_hardware():
    print("\n" + "=" * 60)
    print("[2] PHAN CUNG (CPU & RAM)")
    print("=" * 60)
    cpu_count = os.cpu_count() or 1
    print(f"* So loi CPU      : {cpu_count} cores")
    
    try:
        import psutil
        mem = psutil.virtual_memory()
        print(f"* Tong RAM        : {format_size(mem.total)}")
        print(f"* RAM kha dung    : {format_size(mem.available)} (Dang dung: {mem.percent}%)")
    except ImportError:
        print("* RAM             : (Cai thu vien 'psutil' de xem chi tiet RAM)")

def check_gpu():
    print("\n" + "=" * 60)
    print("[3] KIEM TRA GPU & TANG TOC DO (NVIDIA CUDA)")
    print("=" * 60)
    
    # 1. Check nvidia-smi tool
    nvidia_smi_path = shutil.which("nvidia-smi")
    if nvidia_smi_path:
        print(f"* Da tim thay driver NVIDIA (nvidia-smi): {nvidia_smi_path}")
        try:
            res = subprocess.run(["nvidia-smi", "--query-gpu=name,memory.total,driver_version", "--format=csv,noheader"],
                                 capture_output=True, text=True, check=True)
            for line in res.stdout.strip().splitlines():
                print(f"  -> GPU: {line}")
        except Exception as e:
            print(f"  -> Khong truy van duoc thong tin chi tiet GPU: {e}")
    else:
        print("* Khong phat hien tien ich 'nvidia-smi' (May dung GPU AMD/Intel hoac chi chay CPU).")

    # 2. Check PyTorch CUDA availability if installed
    try:
        import torch
        print(f"* Thu vien PyTorch : Phien ban {torch.__version__}")
        cuda_avail = torch.cuda.is_available()
        print(f"* CUDA kha dung    : {'[CO SAN]' if cuda_avail else '[KHONG CO SAN - Chay CPU mode]'}")
        if cuda_avail:
            print(f"  -> Thiet bi GPU  : {torch.cuda.get_device_name(0)}")
            print(f"  -> Phien ban CUDA: {torch.version.cuda}")
    except ImportError:
        print("* Thu vien PyTorch : Chua cai dat (Se cai o cac giai doan sau).")

def check_core_tools():
    print("\n" + "=" * 60)
    print("[4] CAC CONG CU DANH CHO KY SU (CLI TOOLS)")
    print("=" * 60)
    tools = ["git", "docker", "docker-compose"]
    for tool in tools:
        path = shutil.which(tool)
        if path:
            print(f"* {tool:<15}: [OK] Tim thay ({path})")
        else:
            print(f"* {tool:<15}: [!] Chua cai dat hoac chua them vao PATH")

if __name__ == "__main__":
    check_system()
    check_hardware()
    check_gpu()
    check_core_tools()
    print("\n" + "=" * 60)
    print("Loi khuyen ky thuat tu Mi AI:")
    print("1. Luon su dung moi truong ao rieng biet (.venv) cho tung du an AI.")
    print("2. Dung cai goi thu vien bua bai vao moi truong Python goc cua may tinh.")
    print("=" * 60)
