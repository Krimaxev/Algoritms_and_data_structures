import unittest
from lab_3.task_1.src.main_1 import quicksort_standard,quicksort_threeway


class TestSorting(unittest.TestCase):

    def test_empty_array(self):
        arr = []
        quicksort_threeway(arr)
        quicksort_standard(arr)
        self.assertEqual(arr, [])

    def test_single_element_array(self):
        arr = [5]
        quicksort_threeway(arr)
        quicksort_standard(arr)
        self.assertEqual(arr, [5])

    def test_sorted_array(self):
        arr = [1, 2, 3, 4, 5]
        quicksort_threeway(arr.copy())
        quicksort_standard(arr.copy())
        self.assertEqual(arr, [1, 2, 3, 4, 5])


    def test_array_with_duplicates(self):
        arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4,5]
        sorted_arr = sorted(arr.copy())
        quicksort_threeway(arr.copy())
        quicksort_standard(arr.copy())
        self.assertEqual(arr, sorted_arr)


if __name__ == '__main__':
    unittest.main()
