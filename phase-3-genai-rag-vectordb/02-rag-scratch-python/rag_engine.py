"""
Lab 2: 100% Code Chay RAG (Retrieval-Augmented Generation) in Pure Python
Hiểu cặn kẽ từng bước: Chunking -> Vector Search -> Context Injection -> LLM Prompt
"""
import math
import sys

# Ensure UTF-8 output on Windows
if hasattr(sys.stdout, 'reconfigure'):
    try: sys.stdout.reconfigure(encoding='utf-8')
    except Exception: pass

# 1. Dữ liệu mẫu (Giả lập sổ tay nghiệp vụ ngân hàng)
DOCUMENTS = [
    "Quy định 101: Hạn mức chuyển khoản tối đa qua ứng dụng ngân hàng di động là 500,000,000 VND mỗi ngày đối với khách hàng VIP.",
    "Quy định 102: Để vay tín chấp theo lương, khách hàng cần có thu nhập tối thiểu 10,000,000 VND/tháng và hợp đồng lao động từ 12 tháng trở lên.",
    "Quy định 103: Thời gian làm việc của chi nhánh ngân hàng từ thứ 2 đến thứ 6, sáng 8h00 - 12h00, chiều 13h00 - 17h00.",
    "Quy định 104: Phí duy trì tài khoản thanh toán là 11,000 VND/tháng nếu số dư bình quân tháng dưới 2,000,000 VND."
]

def simple_embed(text: str) -> dict:
    """Giả lập hàm băm từ vựng (Bag of Words / TF) thành vector số học đơn giản"""
    words = text.lower().replace(":", "").replace(",", "").replace(".", "").split()
    vector = {}
    for w in words:
        vector[w] = vector.get(w, 0) + 1
    return vector

def cosine_similarity(v1: dict, v2: dict) -> float:
    """Tính toán độ tương đồng Cosine giữa 2 vector"""
    intersection = set(v1.keys()) & set(v2.keys())
    numerator = sum([v1[x] * v2[x] for x in intersection])

    sum1 = sum([v1[x]**2 for x in v1.keys()])
    sum2 = sum([v2[x]**2 for x in v2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    return float(numerator) / denominator

class ScratchRAG:
    def __init__(self):
        self.vectors = []
        self.docs = []

    def index(self, docs):
        self.docs = docs
        self.vectors = [simple_embed(d) for d in docs]
        print(f" Đã đánh chỉ mục {len(docs)} đoạn tài liệu vào Vector Store!")

    def retrieve(self, query: str, top_k: int = 2):
        q_vec = simple_embed(query)
        scores = []
        for i, doc_vec in enumerate(self.vectors):
            sim = cosine_similarity(q_vec, doc_vec)
            scores.append((sim, self.docs[i]))
        scores.sort(key=lambda x: x[0], reverse=True)
        return scores[:top_k]

    def generate_augmented_prompt(self, query: str) -> str:
        hits = self.retrieve(query, top_k=2)
        context = "\n".join([f"- {h[1]} (Score: {h[0]:.2f})" for h in hits])
        prompt = f"""[SYSTEM PROMPT]
Bạn là trợ lý AI Ngân hàng thông minh. Hãy trả lời câu hỏi của khách hàng DỰA VÀO CÁC TÀI LIỆU SAU:
{context}

[CÂU HỎI KHÁCH HÀNG]
{query}

[CÂU TRẢ LỜI]
"""
        return prompt

if __name__ == "__main__":
    print("=" * 60)
    print("🔬 CHẠY THỬ NGHIỆM RAG 'CODE CHAY' PYTHON THUẦN")
    print("=" * 60)

    rag = ScratchRAG()
    rag.index(DOCUMENTS)

    sample_query = "Điều kiện để tôi vay tín chấp theo lương là gì?"
    print(f"\n🔍 Câu hỏi truy vấn: '{sample_query}'")
    
    hits = rag.retrieve(sample_query, top_k=1)
    print(f"• Đoạn trích khớp nhất: {hits[0][1]} (Điểm: {hits[0][0]:.3f})")

    augmented_prompt = rag.generate_augmented_prompt(sample_query)
    print("\n📝 Prompt sau khi Augmentation (Gắn Context vào Prompt):")
    print("-" * 60)
    print(augmented_prompt)
    print("-" * 60)
    print("🎯 BÀI HỌC: Bản chất của RAG chính là tìm Top Chunks tương đồng nhất và nhồi vào Context Window của LLM!")
