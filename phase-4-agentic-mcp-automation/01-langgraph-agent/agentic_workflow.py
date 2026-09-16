"""
Lab 1: Agentic Workflow with LangGraph StateGraph
Mô phỏng Router Agent tự động phân loại intent và định tuyến công việc
"""
import sys

# Ensure UTF-8 output on Windows
if hasattr(sys.stdout, 'reconfigure'):
    try: sys.stdout.reconfigure(encoding='utf-8')
    except Exception: pass

def simulate_agentic_workflow(user_query: str):
    print("=" * 60)
    print(f"🤖 KHỞI CHẠY AGENTIC GRAPH CHO YÊU CẦU: '{user_query}'")
    print("=" * 60)

    # 1. State Object
    state = {
        "query": user_query,
        "intent": None,
        "tool_output": None,
        "final_response": None
    }
    print("1. [State Initialized] Khởi tạo trạng thái phiên làm việc.")

    # 2. Node Router: Phân tích intent
    print("2. [Router Node] Đang phân tích ý định người dùng...")
    if any(w in user_query.lower() for w in ["tỷ giá", "usd", "ngoại tệ"]):
        state["intent"] = "check_currency"
    elif any(w in user_query.lower() for w in ["vay", "lãi suất", "quy định"]):
        state["intent"] = "query_rag_docs"
    else:
        state["intent"] = "general_chat"

    print(f"   -> Phân loại Intent: '{state['intent']}'")

    # 3. Conditional Edge & Tool Execution
    if state["intent"] == "check_currency":
        print("3. [Tool Node: Exchange Rate] Đang gọi API ngân hàng...")
        state["tool_output"] = {"USD_VND": 25450, "updated_at": "Today"}
        state["final_response"] = f"Tỷ giá USD/VND hôm nay được ghi nhận là {state['tool_output']['USD_VND']:,} VND."
    elif state["intent"] == "query_rag_docs":
        print("3. [Tool Node: Vector DB RAG] Đang truy xuất tài liệu nội bộ...")
        state["tool_output"] = "Điều kiện vay tín chấp: Thu nhập từ 10tr/tháng."
        state["final_response"] = f"Theo quy chế ngân hàng: {state['tool_output']}"
    else:
        print("3. [LLM Direct Chat Node] Trả lời trực tiếp bằng kiến thức chung.")
        state["final_response"] = "Xin chào! Tôi có thể giúp gì cho bạn về các dịch vụ tài chính ngân hàng hôm nay?"

    print("-" * 60)
    print(f"🎉 [KẾT QUẢ CUỐI CÙNG]: {state['final_response']}")
    print("=" * 60)

if __name__ == "__main__":
    simulate_agentic_workflow("Tỷ giá USD hôm nay tại ngân hàng là bao nhiêu?")
    print()
    simulate_agentic_workflow("Tôi muốn hỏi về điều kiện vay tín chấp.")
