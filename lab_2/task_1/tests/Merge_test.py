from lab_2.task_1.src.main_1 import *
import unittest
class TestMergeSort(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(Merge_sort([]), [])

    def test_single_element(self):
        self.assertEqual(Merge_sort([1]), [1])

    def test_sorted_list(self):
        self.assertEqual(Merge_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        self.assertEqual(Merge_sort([4, 3, 2, 1]), [1, 2, 3, 4])

    def test_unsorted_list(self):
        self.assertEqual(Merge_sort([3, 1, 4, 1, 5, 9, 2, 6]), [1, 1, 2, 3, 4, 5, 6, 9])

    def test_duplicates(self):
        self.assertEqual(Merge_sort([1, 3, 2, 3, 1]), [1, 1, 2, 3, 3])

if __name__ == '__main__':
    unittest.main()