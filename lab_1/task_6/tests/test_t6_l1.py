import unittest
from lab_1.task_6.src.task6 import bubble_sort
import resource
import time

class TestBubbleSort(unittest.TestCase):
    def test_empty_list(self):
        # Given
        start = []
        expected = []
        # When
        result = bubble_sort(start)
        # Then
        self.assertEqual(result, expected)

    def test_single_element(self):
        # Given
        start = [1]
        expected = [1]
        # When
        result = bubble_sort(start)
        # Then
        self.assertEqual(result, expected)

    def test_sorted_list(self):
        # Given
        start = [1, 2, 3]
        expected = [1, 2, 3]
        # When
        result = bubble_sort(start)
        # Then
        self.assertEqual(result, expected)

    def test_unsorted_list(self):
        # Given
        start = [3, 2, 1]
        expected = [1, 2, 3]
        # When
        result = bubble_sort(start)
        # Then
        self.assertEqual(result, expected)

    def test_duplicates(self):
        # Given
        start = [3, 1, 2, 1, 3]
        expected = [1, 1, 2, 3, 3]
        # When
        result = bubble_sort(start)
        # Then
        self.assertEqual(result, expected)

    def test_memory_and_time_consumption(self):
        # Given
        input_data = [i for i in range(1000, 0, -1)]  # Reverse sorted list
        start_time = time.time()
        start_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        # When
        result = bubble_sort(input_data)
        end_time = time.time()
        end_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        elapsed_time = end_time - start_time
        memory_usage = end_memory - start_memory
        # Then
        print(f"Execution time: {elapsed_time:.5f} seconds.")
        print(f"Memory usage: {memory_usage} MB.")
        self.assertEqual(result, sorted(input_data))

if __name__ == "__main__":
    unittest.main()