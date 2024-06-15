import unittest
import requests

class TestSystemMonitor(unittest.TestCase):
    def test_system_monitor(self):
        response = requests.get('http://localhost:5000/system_monitor')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('cpu_usage', data)
        self.assertIn('memory_info', data)
        self.assertIn('disk_usage', data)

if __name__ == '__main__':
    unittest.main()

