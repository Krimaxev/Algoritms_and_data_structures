import unittest
from lab_2.task_4.src.main_4 import binary_search
import resource
import time

class TestBinarySearch(unittest.TestCase):
    def test_found(self):
        # Given
        arr = [1, 2, 3, 4, 5]
        target = 3
        # When
        result = binary_search(arr, target)
        # Then
        self.assertEqual(result, 2)

    def test_not_found(self):
        # Given
        arr = [1, 2, 3, 4, 5]
        target = 6
        # When
        result = binary_search(arr, target)
        # Then
        self.assertEqual(result, -1)

    def test_empty_list(self):
        # Given
        arr = []
        target = 1
        # When
        result = binary_search(arr, target)
        # Then
        self.assertEqual(result, -1)

    def test_first_element(self):
        # Given
        arr = [1, 2, 3, 4, 5]
        target = 1
        # When
        result = binary_search(arr, target)
        # Then
        self.assertEqual(result, 0)

    def test_last_element(self):
        # Given
        arr = [1, 2, 3, 4, 5]
        target = 5
        # When
        result = binary_search(arr, target)
        # Then
        self.assertEqual(result, 4)

    def test_memory_and_time_consumption(self):
        # Given
        arr = [i for i in range(1, 1000001)]
        target = 999999
        start_time = time.time()
        start_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        # When
        result = binary_search(arr, target)
        end_time = time.time()
        end_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        elapsed_time = end_time - start_time
        memory_usage = end_memory - start_memory
        # Then
        print(f"Execution time: {elapsed_time:.5f} seconds")
        print(f"Memory usage: {(memory_usage)/1024} MB")
        self.assertEqual(result, 999998)

if __name__ == '__main__':
    unittest.main()