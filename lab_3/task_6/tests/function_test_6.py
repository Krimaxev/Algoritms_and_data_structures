import unittest
from lab_3.task_6.scr.main_6 import sort_z
import resource
import time


class TestSortZ(unittest.TestCase):
    def test_empty_lists(self):
        # Given
        list_a = []
        list_b = []
        # When
        result = sort_z(list_a, list_b)
        # Then
        self.assertEqual(result, 0)

        # Additional test cases
        list_a = [1, 2]
        self.assertEqual(sort_z(list_a, list_b), 0)

        list_b = [1, 2]
        list_a = []
        self.assertEqual(sort_z(list_a, list_b), 0)

    def test_small_lists(self):
        # Given
        list_a = [1, 2]
        list_b = [3, 4]
        # When
        result = sort_z(list_a, list_b)
        # Then
        self.assertEqual(result, 3)

        # Additional case
        list_a = [2, 3]
        list_b = [4, 5]
        self.assertEqual(sort_z(list_a, list_b), 8)

    def test_larger_lists(self):
        # Given
        list_a = [1, 2, 3]
        list_b = [4, 5, 6]
        # When
        result = sort_z(list_a, list_b)
        # Then
        self.assertEqual(result, 4)

    def test_memory_and_time_consumption(self):
        # Given
        list_a = [x for x in range(100)]
        list_b = [y for y in range(100, 200)]
        start_time = time.time()
        start_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        # When
        result = sort_z(list_a, list_b)
        end_time = time.time()
        end_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        elapsed_time = end_time - start_time
        memory_usage = end_memory - start_memory
        # Then
        print(f"Execution time: {elapsed_time:.5f} seconds")
        print(f"Memory usage: {(memory_usage)/2**11} MB")
        self.assertGreater(result, 0)


if __name__ == '__main__':
    unittest.main()