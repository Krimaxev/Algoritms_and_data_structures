import unittest
import resource
import time
from lab_5.task1.src.main import heap


class TestHeap(unittest.TestCase):
    def test_heap_valid(self):
        # Input data
        n = 5
        elements = [1, 3, 2, 5, 4]
        expected_result = "YES"

        # Given:
        result = heap(n, elements)

        # Then:
        self.assertEqual(result, expected_result)

    def test_heap_invalid(self):
        # Input data
        n = 5
        elements = [1, 0, 1, 2, 0]
        expected_result = "NO"

        # Given:
        result = heap(n, elements)

        # Then:
        self.assertEqual(result, expected_result)

    def test_empty(self):
        # Input data
        n = 0
        elements = []
        expected_result = "YES"

        # Given:
        result = heap(n, elements)

        # Then:
        self.assertEqual(result, expected_result)

    def test_performance(self):
        # Input data
        n = 100000
        elements = list(range(1, 100001))

        start_time = time.time()
        start_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

        # Given:
        result = heap(n, elements)

        end_time = time.time()
        end_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

        # Then:
        self.assertEqual(result, "YES")
        print(f"Execution Time: {end_time - start_time} seconds")
        print(f"Memory Usage: {end_memory - start_memory} KB")


if __name__ == "__main__":
    unittest.main()