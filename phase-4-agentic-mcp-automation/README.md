# 🤖 Giai Đoạn 4: Agentic AI, Model Context Protocol (MCP) & Tự Động Hóa

> *"Tương lai của AI không phải là Chatbot chỉ biết gõ chữ, mà là Agentic AI biết tự suy nghĩ, tự lập kế hoạch và chủ động gọi công cụ để giải quyết công việc trọn vẹn."* — Định hướng phát triển từ **Mì AI**

---

## 🎯 Mục Tiêu Giai Đoạn 4
1. **Làm chủ quy trình Agentic AI với LangGraph:**
   * Hiểu StateGraph, Nodes, Edges và Conditional Routers.
   * Xây dựng cơ chế vòng lặp phản hồi (Feedback Loops) và Human-in-the-loop.
2. **Chuẩn hóa kết nối công cụ với Model Context Protocol (MCP):**
   * Tự viết MCP Server bằng Python (FastMCP) chỉ trong vài phút.
   * Kết nối MCP Server với Claude Desktop, Cursor IDE hoặc custom agent.
3. **Tự động hóa quy trình với n8n:**
   * Triển khai n8n qua Docker Compose, tích hợp Gemini AI node và tự động bắn thông báo webhook.

---

## 📂 Danh Sách Bài Thực Hành (Labs)
* **`01-langgraph-agent/`**: Xây dựng StateGraph đa tác tử phân luồng quyết định.
* **`02-fastmcp-server/`**: Viết MCP Server cung cấp dịch vụ tra cứu tỷ giá & số dư ngân hàng.
* **`03-n8n-automation/`**: Cụm n8n Docker Compose tích hợp AI tự động hóa.
