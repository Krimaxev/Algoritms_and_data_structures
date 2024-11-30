import unittest
from lab_4.task_9.src.main import process_requests

class TestProcessRequests(unittest.TestCase):
    def test_example_case(self):
        n = 7
        requests = ["+ 1", "+ 2", "-", "+ 3", "+ 4", "-", "-"]
        self.assertEqual(process_requests(n, requests), ["1", "2", "3"])

    def test_with_middle_insert(self):
        n = 6
        requests = ["+ 1", "+ 2", "* 3", "+ 4", "-", "-"]
        self.assertEqual(process_requests(n, requests), ["1", "3"])

    def test_empty_result(self):
        n = 3
        requests = ["+ 1", "+ 2", "+ 3"]
        self.assertEqual(process_requests(n, requests), [])

    def test_no_requests(self):
        n = 0
        requests = []
        self.assertEqual(process_requests(n, requests), [])

    def test_only_removal(self):
        n = 3
        requests = ["-", "-", "-"]
        self.assertRaises(IndexError, process_requests, n, requests)

if __name__ == "__main__":
    unittest.main()
