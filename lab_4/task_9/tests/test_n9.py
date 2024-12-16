import unittest
import resource
import time
from lab_4.task_9.src.main import process_requests


class TestProcessRequests(unittest.TestCase):
    def test_example_case(self):
        # Input data
        n = 7
        requests = ["+ 1", "+ 2", "-", "+ 3", "+ 4", "-", "-"]
        expected_result = ["1", "2", "3"]

        # Given:
        result = process_requests(n, requests)

        # Then:
        self.assertEqual(result, expected_result)

    def test_with_middle_insert(self):
        # Input data
        n = 6
        requests = ["+ 1", "+ 2", "* 3", "+ 4", "-", "-"]
        expected_result = ["1", "3"]

        # Given:
        result = process_requests(n, requests)

        # Then:
        self.assertEqual(result, expected_result)

    def test_empty_result(self):
        # Input data
        n = 3
        requests = ["+ 1", "+ 2", "+ 3"]
        expected_result = []

        # Given:
        result = process_requests(n, requests)

        # Then:
        self.assertEqual(result, expected_result)

    def test_no_requests(self):
        # Input data
        n = 0
        requests = []
        expected_result = []

        # Given:
        result = process_requests(n, requests)

        # Then:
        self.assertEqual(result, expected_result)

    def test_only_removal(self):
        # Input data
        n = 3
        requests = ["-", "-", "-"]

        # Given:
        # Then:
        self.assertRaises(IndexError, process_requests, n, requests)

    def test_performance(self):
        # Input data
        n = 100000
        requests = ["+ " + str(i) for i in range(n)] + ["-"] * n

        start_time = time.time()
        start_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

        # Given:
        result = process_requests(n, requests)

        end_time = time.time()
        end_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

        # Then:
        self.assertEqual(len(result), n)
        print(f"Execution Time: {end_time - start_time} seconds")
        print(f"Memory Usage: {end_memory - start_memory} KB")


if __name__ == "__main__":
    unittest.main()
