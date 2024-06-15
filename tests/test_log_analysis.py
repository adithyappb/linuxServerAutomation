import unittest
from python_scripts.log_analysis import analyze_logs

class TestLogAnalysis(unittest.TestCase):
    def test_analyze_logs(self):
        result = analyze_logs()
        self.assertIsInstance(result, dict)
        self.assertIn('error_count', result['some_log_file.log'])
        self.assertIn('warning_count', result['some_log_file.log'])

if __name__ == '__main__':
    unittest.main()

