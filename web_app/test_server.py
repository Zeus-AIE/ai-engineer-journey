"""
Automated Test Suite for AI Engineer Roadmap Web Server & API
"""
import unittest
import threading
import urllib.request
import urllib.error
import json
import time
import os
import sys

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from server import start_server, HTTPServer, RoadmapHTTPHandler

TEST_PORT = 8899

class TestRoadmapWebServer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Start server in a background daemon thread
        cls.server = HTTPServer(("", TEST_PORT), RoadmapHTTPHandler)
        cls.server_thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.server_thread.start()
        time.sleep(0.5)  # Wait for server to bind

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()

    def test_01_get_roadmap_api(self):
        url = f"http://localhost:{TEST_PORT}/api/roadmap"
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as resp:
            self.assertEqual(resp.status, 200)
            data = json.loads(resp.read().decode("utf-8"))
            self.assertIn("phases", data)
            self.assertEqual(len(data["phases"]), 5)
            self.assertEqual(data["phases"][0]["id"], 1)
            self.assertTrue(len(data["phases"][0]["labs"]) > 0)

    def test_02_get_system_specs_api(self):
        url = f"http://localhost:{TEST_PORT}/api/system"
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as resp:
            self.assertEqual(resp.status, 200)
            data = json.loads(resp.read().decode("utf-8"))
            self.assertIn("os", data)
            self.assertIn("python_version", data)
            self.assertIn("cpu_cores", data)
            self.assertIn("cuda_ready", data)

    def test_03_progress_get_and_post(self):
        # 1. Post an update
        post_url = f"http://localhost:{TEST_PORT}/api/progress"
        payload = json.dumps({"p1_lab1": True, "test_custom_lab": True}).encode("utf-8")
        req = urllib.request.Request(post_url, data=payload, headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req) as resp:
            self.assertEqual(resp.status, 200)
            res_data = json.loads(resp.read().decode("utf-8"))
            self.assertTrue(res_data["success"])
            self.assertTrue(res_data["progress"]["p1_lab1"])
            self.assertTrue(res_data["progress"]["test_custom_lab"])

        # 2. Get progress
        get_url = f"http://localhost:{TEST_PORT}/api/progress"
        with urllib.request.urlopen(get_url) as resp:
            self.assertEqual(resp.status, 200)
            data = json.loads(resp.read().decode("utf-8"))
            self.assertTrue(data.get("p1_lab1"))

    def test_04_static_index_html(self):
        url = f"http://localhost:{TEST_PORT}/"
        with urllib.request.urlopen(url) as resp:
            self.assertEqual(resp.status, 200)
            html = resp.read().decode("utf-8")
            self.assertIn("<!DOCTYPE html>", html)
            self.assertIn("AI Engineer Journey", html)

    def test_05_not_found_endpoint(self):
        url = f"http://localhost:{TEST_PORT}/api/non_existent_endpoint"
        with self.assertRaises(urllib.error.HTTPError) as ctx:
            urllib.request.urlopen(url)
        self.assertEqual(ctx.exception.code, 404)

if __name__ == "__main__":
    unittest.main()
