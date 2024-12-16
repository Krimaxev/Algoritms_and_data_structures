import unittest
from lab_3.task_1.src.main_1 import quicksort_standard, quicksort_threeway
import resource
import time

class TestSorting(unittest.TestCase):

    def test_empty_array(self):
        # Given
        arr = []
        # When
        quicksort_threeway(arr)
        quicksort_standard(arr)
        # Then
        self.assertEqual(arr, [])

    def test_single_element_array(self):
        # Given
        arr = [5]
        # When
        quicksort_threeway(arr)
        quicksort_standard(arr)
        # Then
        self.assertEqual(arr, [5])

    def test_sorted_array(self):
        # Given
        arr = [1, 2, 3, 4, 5]
        arr_copy1 = arr.copy()
        arr_copy2 = arr.copy()
        # When
        quicksort_threeway(arr_copy1)
        quicksort_standard(arr_copy2)
        # Then
        self.assertEqual(arr_copy1, [1, 2, 3, 4, 5])
        self.assertEqual(arr_copy2, [1, 2, 3, 4, 5])

    def test_array_with_duplicates(self):
        # Given
        arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]
        sorted_arr = sorted(arr.copy())
        arr_copy1 = arr.copy()
        arr_copy2 = arr.copy()
        # When
        quicksort_threeway(arr_copy1)
        quicksort_standard(arr_copy2)
        # Then
        self.assertEqual(arr_copy1, sorted_arr)
        self.assertEqual(arr_copy2, sorted_arr)

    def test_memory_and_time_consumption(self):
        # Given
        arr = [i for i in range(1001, 0, -1)]
        arr_copy1 = arr.copy()
        arr_copy2 = arr.copy()
        start_time = time.time()
        start_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        # When
        quicksort_threeway(arr_copy1)
        quicksort_standard(arr_copy2)
        end_time = time.time()
        end_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        elapsed_time = end_time - start_time
        memory_usage = end_memory - start_memory
        # Then
        print(f"Execution time: {elapsed_time:.5f} seconds")
        print(f"Memory usage: {(memory_usage)/1024} MB")
        self.assertEqual(arr_copy1, sorted(arr))
        self.assertEqual(arr_copy2, sorted(arr))

if __name__ == '__main__':
    unittest.main()