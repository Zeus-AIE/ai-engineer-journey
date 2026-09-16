# 🧠 Giai Đoạn 3: Kỷ Nguyên GenAI - LLM, Vector Database & RAG Chuyên Sâu

> *"80% chất lượng của một hệ thống RAG không nằm ở LLM, mà nằm ở khâu bóc tách tài liệu (Parsing) và chiến lược cắt đoạn (Chunking)."* — Triết lý thực chiến từ **Mì AI**

---

## 🎯 Mục Tiêu Giai Đoạn 3
1. **Làm chủ khâu xử lý tài liệu thô:**
   * Dùng **IBM Docling** để parse các tài liệu PDF phức tạp chứa bảng biểu ngân hàng, tài chính.
   * Hiểu các chiến lược Chunking: Fixed-size, Semantic, Recursive.
2. **Xây dựng RAG 'Code Chay' Python thuần:**
   * Không phụ thuộc vào LangChain hay LlamaIndex ở giai đoạn học để hiểu tường tận:
     * Embedding Model sinh vector như thế nào?
     * Thuật toán Cosine Similarity quét dữ liệu trong Vector DB ra sao?
     * Context Injection vào System Prompt được thực hiện như thế nào?
3. **Tối ưu chi phí và độ trễ với Prompt Caching:**
   * Giảm 80% chi phí token API khi gọi Gemini / Claude / OpenAI đối với kho tài liệu cố định.
4. **Fine-tuning mô hình Embedding:**
   * Tinh chỉnh không gian vector bằng MultipleNegativesRankingLoss cho tiếng Việt.

---

## 📂 Danh Sách Bài Thực Hành (Labs)
* **`01-docling-parser/`**: Bóc tách tài liệu phức tạp sang Markdown cấu trúc cao.
* **`02-rag-scratch-python/`**: RAG hoàn chỉnh viết bằng Python thuần + Vector Search.
* **`03-prompt-caching/`**: Kỹ thuật Context Caching tiết kiệm chi phí token.
* **`04-embedding-finetune/`**: Huấn luyện Fine-tune Sentence Transformers trên Colab/Local GPU.
