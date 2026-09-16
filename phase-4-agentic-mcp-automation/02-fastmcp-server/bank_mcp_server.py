"""
Lab 2: Model Context Protocol (MCP) Server
Tạo một MCP Server cung cấp các công cụ ngân hàng cho Claude Desktop, Cursor IDE hoặc AI Agent
"""
import sys
import json

# Ensure UTF-8 output on Windows
if hasattr(sys.stdout, 'reconfigure'):
    try: sys.stdout.reconfigure(encoding='utf-8')
    except Exception: pass

def main():
    print("=" * 60)
    print("🔌 MODEL CONTEXT PROTOCOL (MCP) SERVER")
    print("=" * 60)
    print("""
Cách hoạt động của Model Context Protocol:
- MCP sử dụng JSON-RPC 2.0 qua Standard I/O hoặc SSE (Server-Sent Events).
- Client (Cursor / Claude / Agent) gửi lệnh 'tools/list' để khám phá các công cụ.
- Khi người dùng hỏi, Client gửi lệnh 'tools/call' kèm tham số JSON.

Code mẫu triển khai với FastMCP (chuẩn 2026):

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("BankingServices")

@mcp.tool()
def get_exchange_rate(currency: str) -> float:
    '''Tra cứu tỷ giá ngoại tệ hôm nay so với VND'''
    rates = {"USD": 25450.0, "EUR": 27200.0, "JPY": 165.5}
    return rates.get(currency.upper(), 0.0)

@mcp.tool()
def check_account_balance(account_id: str) -> dict:
    '''Kiểm tra số dư khả dụng của tài khoản khách hàng'''
    return {"account_id": account_id, "balance_vnd": 15000000, "currency": "VND"}

if __name__ == "__main__":
    mcp.run()
    """)
    print("=" * 60)
    print("🎯 BÀI HỌC TỪ MÌ AI:")
    print("Chỉ cần viết 1 file MCP Server duy nhất, bạn có thể cắm công cụ này vào cả Claude,")
    print("Cursor IDE và bot chat riêng của công ty mà không cần sửa 1 dòng code logic!")
    print("=" * 60)

if __name__ == "__main__":
    main()
