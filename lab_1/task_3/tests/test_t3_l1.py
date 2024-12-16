import unittest
import resource
import time
from lab_1.task_3.src.task3 import insertion_sort_three

class TestInsertionSort(unittest.TestCase):
    def test_sort_empty(self):
        # Given
        start = []
        finish = []
        # When
        result = insertion_sort_three(start)
        # Then
        self.assertEqual(result, finish)

    def test_sort_single_element(self):
        # Given
        start = [1]
        finish = [1]
        # When
        result = insertion_sort_three(start)
        # Then
        self.assertEqual(result, finish)

    def test_sort_sorted(self):
        # Given
        start = [1, 2, 3, 4, 5]
        finish = [5, 4, 3, 2, 1]
        # When
        result = insertion_sort_three(start)
        # Then
        self.assertEqual(result, finish)

    def test_sort_reverse_sorted(self):
        # Given
        start = [5, 4, 3, 2, 1]
        finish = [5, 4, 3, 2, 1]
        # When
        result = insertion_sort_three(start)
        # Then
        self.assertEqual(result, finish)

    def test_sort_unsorted(self):
        # Given
        start = [3, 1, 4, 2, 5]
        finish = [5, 4, 3, 2, 1]
        # When
        result = insertion_sort_three(start)
        # Then
        self.assertEqual(result, finish)

    def test_sort_with_duplicates(self):
        # Given
        start = [3, 1, 2, 3, 3]
        finish = [3, 3, 3, 2, 1]
        # When
        result = insertion_sort_three(start)
        # Then
        self.assertEqual(result, finish)

    def test_sort_negative_numbers(self):
        # Given
        start = [-1, -3, 2, 1, 0]
        finish = [2, 1, 0, -1, -3]
        # When
        result = insertion_sort_three(start)
        # Then
        self.assertEqual(result, finish)

    def test_sort_large_numbers(self):
        # Given
        start = [1000, 500, 100, 0, 200]
        finish = [1000, 500, 200, 100, 0]
        # When
        result = insertion_sort_three(start)
        # Then
        self.assertEqual(result, finish)

    def test_memory_and_time_consumption(self):
        # Given
        input_data = [i for i in range(10000000, 0, -1)]  # Reverse sorted list
        start_time = time.time()
        start_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        # When
        result = insertion_sort_three(input_data)
        end_time = time.time()
        end_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        elapsed_time = end_time - start_time
        memory_usage = end_memory - start_memory
        # Then
        print(f"Execution time: {elapsed_time:.5f} seconds.")
        print(f"Memory usage: {(memory_usage)//2**19} MB.")
        self.assertEqual(result, sorted(input_data, reverse=True))

if __name__ == '__main__':
    unittest.main()