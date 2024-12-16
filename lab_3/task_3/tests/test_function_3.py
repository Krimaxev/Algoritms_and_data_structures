import unittest
from lab_3.task_3.src.main_3 import matreshka
import resource
import time


class TestMatreshka(unittest.TestCase):
    def test_empty_array(self):
        # Given
        arr = []
        size = 2
        k = 0
        # When
        result = matreshka(arr, size, k)
        # Then
        self.assertTrue(result)

    def test_single_element(self):
        # Given
        arr = [5]
        size = 1
        k = 1
        # When
        result = matreshka(arr, size, k)
        # Then
        self.assertTrue(result)

    def test_multiple_of_k(self):
        # Given
        arr1 = [1, 5, 2, 6, 3, 7, 4, 8]
        size1 = 2
        k1 = 8

        arr2 = [1, 4, 7, 2, 5, 8, 3, 6]
        size2 = 4
        k2 = 8
        # When and Then
        self.assertFalse(matreshka(arr1, size1, k1))
        self.assertFalse(matreshka(arr2, size2, k2))

    def test_not_multiple_of_k(self):
        # Given
        arr1 = [1, 5, 2, 6, 3, 7, 4]
        size1 = 2
        k1 = 7

        arr2 = [1, 5, 2, 6, 3, 7]
        size2 = 4
        k2 = 6
        # When and Then
        self.assertFalse(matreshka(arr1, size1, k1))
        self.assertFalse(matreshka(arr2, size2, k2))

    def test_already_sorted(self):
        # Given
        arr = [1, 2, 3, 4]
        size = 2
        k = 4
        # When
        result = matreshka(arr, size, k)
        # Then
        self.assertTrue(result)

    def test_unsorted(self):
        # Given
        arr = [5, 1, 3, 2]
        size = 2
        k = 4
        # When
        result = matreshka(arr, size, k)
        # Then
        self.assertFalse(result)

    def test_memory_and_time_consumption(self):
        # Given
        arr = list(range(1, 1001))
        size = 500
        k = 1000
        start_time = time.time()
        start_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        # When
        result = matreshka(arr, size, k)
        end_time = time.time()
        end_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        elapsed_time = end_time - start_time
        memory_usage = end_memory - start_memory
        # Then
        print(f"Execution time: {elapsed_time:.5f} seconds")
        print(f"Memory usage: {(memory_usage)/1024} MB")
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()