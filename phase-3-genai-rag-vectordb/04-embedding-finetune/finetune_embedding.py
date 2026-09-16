"""
Lab 4: Fine-tuning Embedding Models for Vietnamese Domain
Sử dụng SentenceTransformers và MultipleNegativesRankingLoss
"""
import sys

# Ensure UTF-8 output on Windows
if hasattr(sys.stdout, 'reconfigure'):
    try: sys.stdout.reconfigure(encoding='utf-8')
    except Exception: pass

def main():
    print("=" * 60)
    print("🧬 HUẤN LUYỆN FINE-TUNE EMBEDDING CHO TIẾNG VIỆT")
    print("=" * 60)
    print("""
Quy trình thực tế trên Google Colab / GPU Local (RTX 3060):

1. CHUẨN BỊ DỮ LIỆU CẶP (PAIR DATA):
   Tập dữ liệu câu hỏi - đoạn trích đúng (Anchor - Positive):
   - Anchor: "Hạn mức chuyển tiền tối đa 1 ngày là bao nhiêu?"
   - Positive: "Quy định 101: Hạn mức tối đa 500 triệu đồng..."

2. LOSS FUNCTION:
   Sử dụng MultipleNegativesRankingLoss:
   - Các mẫu khác trong cùng 1 Batch sẽ tự động đóng vai trò là Negative samples.
   - Giúp không gian vector kéo các cặp (Anchor - Positive) lại gần nhau và đẩy xa Negative.

3. MÃ NGUỒN HUẤN LUYỆN:
   from sentence_transformers import SentenceTransformer, InputExample, losses
   from torch.utils.data import DataLoader

   model = SentenceTransformer("bkai-foundation-models/vietnamese-bi-encoder")
   train_loss = losses.MultipleNegativesRankingLoss(model)
   model.fit(train_objectives=[(train_dataloader, train_loss)], epochs=3)
   model.save("vietnamese-embedding-finetuned")
    """)
    print("=" * 60)

if __name__ == "__main__":
    main()
