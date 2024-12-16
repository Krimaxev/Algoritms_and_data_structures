from lab_2.task_1.src.main_1 import merge_sort
import unittest
import resource
import time

class TestMergeSort(unittest.TestCase):

    def test_empty_list(self):
        # Given
        input_data = []
        expected_result = []
        # When
        result = merge_sort(input_data)
        # Then
        self.assertEqual(result, expected_result)

    def test_single_element(self):
        # Given
        input_data = [1]
        expected_result = [1]
        # When
        result = merge_sort(input_data)
        # Then
        self.assertEqual(result, expected_result)

    def test_sorted_list(self):
        # Given
        input_data = [1, 2, 3, 4, 5]
        expected_result = [1, 2, 3, 4, 5]
        # When
        result = merge_sort(input_data)
        # Then
        self.assertEqual(result, expected_result)

    def test_reverse_sorted_list(self):
        # Given
        input_data = [4, 3, 2, 1]
        expected_result = [1, 2, 3, 4]
        # When
        result = merge_sort(input_data)
        # Then
        self.assertEqual(result, expected_result)

    def test_unsorted_list(self):
        # Given
        input_data = [3, 1, 4, 1, 5, 9, 2, 6]
        expected_result = [1, 1, 2, 3, 4, 5, 6, 9]
        # When
        result = merge_sort(input_data)
        # Then
        self.assertEqual(result, expected_result)

    def test_duplicates(self):
        # Given
        input_data = [1, 3, 2, 3, 1]
        expected_result = [1, 1, 2, 3, 3]
        # When
        result = merge_sort(input_data)
        # Then
        self.assertEqual(result, expected_result)

    def test_memory_and_time_consumption(self):
        # Given
        input_data = [i for i in range(1000, 0, -1)]
        start_time = time.time()
        start_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        # When
        result = merge_sort(input_data)
        end_time = time.time()
        end_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        elapsed_time = end_time - start_time
        memory_usage = end_memory - start_memory
        # Then
        print(f"Execution time: {elapsed_time:.5f} seconds.")
        print(f"Memory usage: {(memory_usage)/1024} MB.")
        self.assertEqual(result, sorted(input_data))

if __name__ == '__main__':
    unittest.main()