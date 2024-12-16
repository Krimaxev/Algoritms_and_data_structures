import unittest
import resource
import time
from lab_4.task_7.src.main import max_dynamic_sequence


class TestMaxDynamicSequence(unittest.TestCase):
    def test_case_1(self):
        # Input data
        n = 8
        a = [2, 7, 3, 1, 5, 2, 6, 2]
        m = 4
        expected_result = [7, 7, 5, 6, 6]

        # Given:
        result = max_dynamic_sequence(n, a, m)

        # Then:
        self.assertEqual(result, expected_result)

    def test_case_2(self):
        # Input data
        n = 5
        a = [1, 2, 3, 4, 5]
        m = 2
        expected_result = [2, 3, 4, 5]

        # Given:
        result = max_dynamic_sequence(n, a, m)

        # Then:
        self.assertEqual(result, expected_result)

    def test_case_3(self):
        # Input data
        n = 6
        a = [6, 5, 4, 3, 2, 1]
        m = 3
        expected_result = [6, 5, 4, 3]

        # Given:
        result = max_dynamic_sequence(n, a, m)

        # Then:
        self.assertEqual(result, expected_result)

    def test_performance(self):
        # Input data
        n = 100000
        a = list(range(1, 100001))
        m = 10

        start_time = time.time()
        start_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

        # Given:
        result = max_dynamic_sequence(n, a, m)

        end_time = time.time()
        end_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

        # Then:
        self.assertEqual(len(result), n - m + 1)
        print(f"Execution Time: {end_time - start_time} seconds")
        print(f"Memory Usage: {(end_memory - start_memory)/2**12} MB")


if __name__ == "__main__":
    unittest.main()