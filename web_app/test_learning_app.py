"""
Unit Test Suite for AI Engineer Academy 2026 Web Application
Verifies curriculum integrity, navigation tabs, dedicated theory hub with citations & diagrams,
terminal simulator, quiz datasets, and root/static synchronization.
"""
import unittest
import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INDEX_HTML = os.path.join(BASE_DIR, "static", "index.html")
ROOT_INDEX = os.path.join(os.path.dirname(BASE_DIR), "index.html")

class TestLearningWebApp(unittest.TestCase):
    def setUp(self):
        self.assertTrue(os.path.exists(INDEX_HTML), "web_app/static/index.html file must exist")
        self.assertTrue(os.path.exists(ROOT_INDEX), "Root index.html file must exist for GitHub Pages")
        with open(INDEX_HTML, "r", encoding="utf-8") as f:
            self.html = f.read()
        with open(ROOT_INDEX, "r", encoding="utf-8") as f:
            self.root_html = f.read()

    def test_01_all_navigation_tabs_present(self):
        """Kiểm tra có đầy đủ 7 tab chức năng bao gồm Lý Thuyết Chuyên Sâu"""
        required_tabs = [
            "nav-roadmap", 
            "nav-theory", 
            "nav-terminal", 
            "nav-quiz", 
            "nav-flashcard", 
            "nav-notes", 
            "nav-cert"
        ]
        for tab in required_tabs:
            self.assertIn(f'id="{tab}"', self.html, f"Missing navigation tab: {tab}")

    def test_02_five_phases_curriculum_integrity(self):
        """Kiểm tra đầy đủ 5 Giai đoạn trong bộ dữ liệu JavaScript"""
        for phase_id in [1, 2, 3, 4, 5]:
            self.assertIn(f'"id": {phase_id}', self.html, f"Phase {phase_id} must be defined in roadmap")
        
        self.assertIn("phase-1-foundation", self.html)
        self.assertIn("phase-2-machine-learning-cv", self.html)
        self.assertIn("phase-3-genai-rag-vectordb", self.html)
        self.assertIn("phase-4-agentic-mcp-automation", self.html)
        self.assertIn("phase-5-production-security-mlops", self.html)

    def test_03_dedicated_theory_hub_structure(self):
        """Kiểm tra trang Lý Thuyết Chuyên Sâu có đầy đủ 5 chương chuyên khảo"""
        self.assertIn('id="section-theory"', self.html, "Section theory must exist")
        for p_id in ["p1", "p2", "p3", "p4", "p5"]:
            self.assertIn(f'id="theory-{p_id}"', self.html, f"Theory article for {p_id} must exist")
            self.assertIn(f'id="tnav-{p_id}"', self.html, f"Theory sidebar button for {p_id} must exist")

    def test_04_authoritative_citations_present(self):
        """Kiểm tra các trích dẫn nguồn uy tín và link tham chiếu theo yêu cầu"""
        citations = [
            "docs.nvidia.com/cuda",
            "docs.docker.com",
            "miai.vn",
            "docs.ultralytics.com",
            "fastapi.tiangolo.com",
            "arxiv.org/abs/1706.03762",
            "github.com/DS4SD/docling",
            "anthropic.com",
            "modelcontextprotocol.io",
            "langchain-ai.github.io/langgraph",
            "owasp.org",
            "ollama.com"
        ]
        for cite in citations:
            self.assertIn(cite, self.html, f"Missing citation link: {cite}")

    def test_05_visual_diagrams_and_formulas(self):
        """Kiểm tra có sơ đồ kiến trúc minh họa (ASCII/Flow) và công thức cốt lõi"""
        # CUDA vs CPU diagram
        self.assertIn("3840 CUDA Cores", self.html)
        # YOLO Pipeline
        self.assertIn("CSPDarknet", self.html)
        self.assertIn("Non-Max Suppression", self.html)
        # Transformer Self-Attention formula
        self.assertIn("Attention}(Q, K, V)", self.html)
        # Agent Loop
        self.assertIn("ReAct (Reason + Act)", self.html)
        # Private AI Stack & Security
        self.assertIn("Private AI Stack", self.html)
        self.assertIn("Guardrail Filter Layer", self.html)

    def test_06_terminal_simulator_commands(self):
        """Kiểm tra các lệnh mô phỏng của Terminal Simulator"""
        commands = ["probe", "rag", "guard", "yolo", "cache", "docker", "clear"]
        for cmd in commands:
            self.assertIn(f"lower === '{cmd}'", self.html, f"Terminal must handle command '{cmd}'")

    def test_07_quiz_and_flashcards_structure(self):
        """Kiểm tra dữ liệu trắc nghiệm và flashcards không bị rỗng"""
        self.assertIn("QUIZ_QUESTIONS", self.html)
        self.assertIn("FLASHCARDS", self.html)
        self.assertIn("Attention Is All You Need", self.html)
        self.assertIn("Non-Max Suppression", self.html)

    def test_08_modal_interactive_drawers(self):
        """Kiểm tra 4 tab của cửa sổ học tập chuyên sâu"""
        modal_tabs = ["mtab-theory", "mtab-diagram", "mtab-code", "mtab-interview"]
        for mtab in modal_tabs:
            self.assertIn(f'id="{mtab}"', self.html, f"Modal drawer missing tab: {mtab}")

    def test_09_root_index_synchronized_with_static(self):
        """Đảm bảo root index.html khớp hoàn toàn với web_app/static/index.html phục vụ GitHub Pages"""
        self.assertEqual(len(self.html), len(self.root_html), "Root index.html and static index.html should match")
        self.assertIn('id="section-theory"', self.root_html)

if __name__ == "__main__":
    unittest.main()
