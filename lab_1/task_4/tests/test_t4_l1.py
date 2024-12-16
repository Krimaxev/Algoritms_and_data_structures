import unittest
import resource
import time
from lab_1.task_4.src.task4 import line_find


class TestLineFind(unittest.TestCase):
    def test_no_occurrences(self):
        # Given
        target = 10
        array = [1, 2, 3, 4, 5]
        expected_result = "-1"
        # When
        result = line_find(target, array)
        # Then
        self.assertEqual(result, expected_result)

    def test_one_occurrence(self):
        # Given
        target = 3
        array = [1, 2, 3, 4, 5]
        expected_result = "2"
        # When
        result = line_find(target, array)
        # Then
        self.assertEqual(result, expected_result)

    def test_multiple_occurrences(self):
        # Given
        target = 2
        array = [1, 2, 3, 2, 4, 2]
        expected_result = "3\n1, 3, 5"
        # When
        result = line_find(target, array)
        # Then
        self.assertEqual(result, expected_result)

    def test_memory_and_time_consumption(self):
        # Given
        target = 5
        array = [5] * 1000 + [1, 2, 3, 4, 6]
        start_time = time.time()
        start_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        # When
        result = line_find(target, array)
        end_time = time.time()
        end_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        elapsed_time = end_time - start_time
        memory_usage = end_memory - start_memory
        # Then
        print(f"Execution time: {elapsed_time:.5f} seconds.")
        print(f"Memory usage: {(memory_usage)/1024} MB.")
        self.assertIn("1, 2", result)

if __name__ == "__main__":
    unittest.main()