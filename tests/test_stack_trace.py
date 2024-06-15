import unittest
import requests

class TestStackTrace(unittest.TestCase):
    def test_stack_trace(self):
        response = requests.get('http://localhost:5000/stack_trace')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Stack Trace', response.text)

if __name__ == '__main__':
    unittest.main()

