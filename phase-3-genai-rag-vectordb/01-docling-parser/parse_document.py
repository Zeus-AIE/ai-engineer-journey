"""
Lab 1: Document Parsing with IBM Docling
Chuyển đổi tài liệu PDF phức tạp (chứa bảng biểu) thành Markdown sạch cho LLM
"""
import sys
import os

# Ensure UTF-8 output on Windows
if hasattr(sys.stdout, 'reconfigure'):
    try: sys.stdout.reconfigure(encoding='utf-8')
    except Exception: pass

def main():
    print("=" * 60)
    print("📄 BÓC TÁCH TÀI LIỆU PHỨC TẠP VỚI IBM DOCLING")
    print("=" * 60)

    try:
        from docling.document_converter import DocumentConverter
    except ImportError:
        print("ℹ️ Thư viện 'docling' có thể được cài đặt bằng: pip install docling")
        print("\n💡 Code mẫu hoạt động chuẩn theo hướng dẫn Mì AI:")
        print('''
        from docling.document_converter import DocumentConverter

        converter = DocumentConverter()
        result = converter.convert("bao_cao_tai_chinh.pdf")
        
        # Xuất Markdown sạch giữ nguyên cấu trúc bảng biểu:
        markdown_text = result.document.export_to_markdown()
        print(markdown_text[:500])
        ''')
        return

    converter = DocumentConverter()
    print(" Khởi tạo Docling DocumentConverter thành công!")
    print("Docling tự động bóc tách: Layout Analysis, Table Structure, Reading Order.")

if __name__ == "__main__":
    main()
