# 🎓 Đồ Án Tốt Nghiệp Capstone: Trợ Lý AI Doanh Nghiệp Toàn Diện

Đây là đồ án tổng hợp đỉnh cao giúp bạn khẳng định năng lực **AI Engineer thực chiến** trước các nhà tuyển dụng:

---

## 🏛️ Kiến Trúc Hệ Thống (Architecture Blueprint)

```
[ Khách Hàng / Giao Diện ]
            │ (HTTPS)
            ▼
[ Input Sanitization / Guardrails ]  ──> Phát hiện & Chặn Prompt Injection
            │ (An toàn)
            ▼
[ Router Agent (LangGraph) ] ──┬──> [ Agentic Tool / MCP Server ] ──> Tra cứu SQL / Tỷ giá
                               │
                               └──> [ Advanced RAG Engine ]
                                           │
                                     [ IBM Docling ] (Parse PDF bảng biểu)
                                           │
                                     [ Qdrant / Vector DB ] (Semantic Search)
                                           │
                                     [ Prompt Caching Layer ] (Tiết kiệm 80% chi phí)
                                           │
                                           ▼
                                     [ LLM Serving ] (Local Ollama / Gemini API)
```

---

## 📋 Checklist Tiêu Chuẩn Nộp Đồ Án
- [ ] Mã nguồn được phân chia module sạch trong `src/`.
- [ ] Có file `docker-compose.yml` chạy 1 lệnh là dựng xong toàn bộ hệ thống.
- [ ] Có bộ kiểm thử `pytest` đạt độ bao phủ (coverage) > 80%.
- [ ] Có video demo ngắn 2-3 phút hoặc ảnh chụp kết quả trực quan trên file `README.md`.
