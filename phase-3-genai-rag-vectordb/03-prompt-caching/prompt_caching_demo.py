"""
Lab 3: Prompt Caching & Token Cost Optimization
Phân tích kỹ thuật Context Caching giúp giảm 80% chi phí gọi API LLM
"""
import sys

# Ensure UTF-8 output on Windows
if hasattr(sys.stdout, 'reconfigure'):
    try: sys.stdout.reconfigure(encoding='utf-8')
    except Exception: pass

def calculate_savings(doc_tokens=100000, queries_per_day=500):
    # Giá API tham chiếu thông thường:
    # Không Cache: Input Token = $3.00 / 1M tokens
    # Có Cache   : Cached Write = $3.75 / 1M (lần đầu), Cache Read = $0.30 / 1M (giảm 90%!)
    price_regular_per_m = 3.00
    price_cache_read_per_m = 0.30

    daily_tokens = doc_tokens * queries_per_day
    
    # Chi phí không cache
    cost_no_cache = (daily_tokens / 1_000_000) * price_regular_per_m
    
    # Chi phí có cache: 1 lần write ban đầu + 499 lần read
    cost_cached = (doc_tokens / 1_000_000) * 3.75 + ((doc_tokens * (queries_per_day - 1)) / 1_000_000) * price_cache_read_per_m
    
    savings = cost_no_cache - cost_cached
    percent = (savings / cost_no_cache) * 100

    print("=" * 60)
    print("💰 PHÂN TÍCH TỐI ƯU CHI PHÍ TOKEN VỚI PROMPT CACHING")
    print("=" * 60)
    print(f"• Dung lượng tài liệu tĩnh : {doc_tokens:,} tokens (~250 trang A4)")
    print(f"• Số lượt truy vấn / ngày  : {queries_per_day:,} queries")
    print(f"• Chi phí KHÔNG cache/ngày : ${cost_no_cache:,.2f} USD")
    print(f"• Chi phí CÓ cache/ngày    : ${cost_cached:,.2f} USD")
    print("-" * 60)
    print(f" TIẾT KIỆM ĐƯỢC          : ${savings:,.2f} USD / ngày ({percent:.1f}%)")
    print(f"📈 TIẾT KIỆM HÀNG NĂM      : ${savings * 365:,.2f} USD / năm")
    print("=" * 60)

if __name__ == "__main__":
    calculate_savings()
