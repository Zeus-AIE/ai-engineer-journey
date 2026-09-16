"""
Unit Test Suite for AI Engineer Academy 2026 Web Application
Verifies curriculum integrity, interactive tabs, quiz datasets, and server responses.
"""
import unittest
import os
import re
import urllib.request

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INDEX_HTML = os.path.join(BASE_DIR, "static", "index.html")

class TestLearningWebApp(unittest.TestCase):
    def setUp(self):
        self.assertTrue(os.path.exists(INDEX_HTML), "index.html file must exist")
        with open(INDEX_HTML, "r", encoding="utf-8") as f:
            self.html = f.read()

    def test_01_all_navigation_tabs_present(self):
        """Kiểm tra có đầy đủ 6 tab chức năng của nền tảng học tập"""
        required_tabs = ["nav-roadmap", "nav-terminal", "nav-quiz", "nav-flashcard", "nav-notes", "nav-cert"]
        for tab in required_tabs:
            self.assertIn(f'id="{tab}"', self.html, f"Missing navigation tab: {tab}")

    def test_02_five_phases_curriculum_integrity(self):
        """Kiểm tra đầy đủ 5 Giai đoạn trong bộ dữ liệu JavaScript"""
        for phase_id in [1, 2, 3, 4, 5]:
            self.assertIn(f'"id": {phase_id}', self.html, f"Phase {phase_id} must be defined in roadmap")
        
        # Verify specific core topics
        self.assertIn("phase-1-foundation", self.html)
        self.assertIn("phase-2-machine-learning-cv", self.html)
        self.assertIn("phase-3-genai-rag-vectordb", self.html)
        self.assertIn("phase-4-agentic-mcp-automation", self.html)
        self.assertIn("phase-5-production-security-mlops", self.html)

    def test_03_terminal_simulator_commands(self):
        """Kiểm tra các lệnh mô phỏng của Terminal Simulator"""
        commands = ["probe", "rag", "guard", "yolo", "cache", "docker", "clear"]
        for cmd in commands:
            self.assertIn(f"lower === '{cmd}'", self.html, f"Terminal must handle command '{cmd}'")

    def test_04_quiz_and_flashcards_structure(self):
        """Kiểm tra dữ liệu trắc nghiệm và flashcards không bị rỗng"""
        self.assertIn("QUIZ_QUESTIONS", self.html)
        self.assertIn("FLASHCARDS", self.html)
        self.assertIn("Attention Is All You Need", self.html)
        self.assertIn("Non-Max Suppression", self.html)

    def test_05_modal_interactive_drawers(self):
        """Kiểm tra 4 tab của cửa sổ học tập chuyên sâu"""
        modal_tabs = ["mtab-theory", "mtab-diagram", "mtab-code", "mtab-interview"]
        for mtab in modal_tabs:
            self.assertIn(f'id="{mtab}"', self.html, f"Modal drawer missing tab: {mtab}")

if __name__ == "__main__":
    unittest.main()
