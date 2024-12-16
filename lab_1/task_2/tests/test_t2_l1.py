import unittest
import resource
import time
from lab_1.task_2.src.task2 import insertion_sort_two

class TestInsertionSort(unittest.TestCase):

    def test_empty_list(self):
        # Given
        start = []
        expected = []
        # When
        result = insertion_sort_two(start)
        # Then
        self.assertEqual(result, expected)

    def test_single_element_list(self):
        # Given
        start = [42]
        expected = [0]
        # When
        result = insertion_sort_two(start)
        # Then
        self.assertEqual(result, expected)

    def test_sorted_list(self):
        # Given
        start = [1, 2, 3, 4, 5]
        expected = [0, 1, 2, 3, 4]
        # When
        result = insertion_sort_two(start)
        # Then
        self.assertEqual(result, expected)

    def test_reverse_sorted_list(self):
        # Given
        start = [5, 4, 3, 2, 1]
        expected = [0, 0, 0, 0, 0]
        # When
        result = insertion_sort_two(start)
        # Then
        self.assertEqual(result, expected)

    def test_unsorted_list(self):
        # Given
        start = [3, 1, 4, 2]
        expected = [0, 0, 2, 1]
        # When
        result = insertion_sort_two(start)
        # Then
        self.assertEqual(result, expected)

    def test_duplicates(self):
        # Given
        start = [2, 2, 1]
        expected = [0, 0, 0]
        # When
        result = insertion_sort_two(start)
        # Then
        self.assertEqual(result, expected)

    def test_memory_and_time_consumption(self):
        # Given
        input_data = [i for i in range(1000, 0, -1)]  # Reverse sorted list
        start_time = time.time()
        start_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        # When
        result = insertion_sort_two(input_data)
        end_time = time.time()
        end_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        elapsed_time = end_time - start_time
        memory_usage = end_memory - start_memory
        # Then
        print(f"Execution time: {elapsed_time:.5f} seconds.")
        print(f"Memory usage: {memory_usage} KB.")
        self.assertEqual(len(result), len(input_data))

if __name__ == '__main__':
    unittest.main()