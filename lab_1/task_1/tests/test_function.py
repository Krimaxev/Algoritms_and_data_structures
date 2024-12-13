import unittest
from lab_1.task_1.src.task1 import insertion_sort

class TestInsertionSort(unittest.TestCase):
    def test_sorted_list(self):
        start = [1, 2, 3, 4, 5]
        finish = [1, 2, 3, 4, 5]
        self.assertEqual(insertion_sort(start), finish)

    def test_reverse_sorted_list(self):
        start = [5, 4, 3, 2, 1]
        finish = [1, 2, 3, 4, 5]
        self.assertEqual(insertion_sort(start), finish)

    def test_unsorted_list(self):
        start = [3, 1, 4, 2, 5]
        finish = [1, 2, 3, 4, 5]
        self.assertEqual(insertion_sort(start), finish)

    def test_empty_list(self):
        start = []
        finish = []
        self.assertEqual(insertion_sort(start), finish)

    def test_single_element_list(self):
        start = [42]
        finish = [42]
        self.assertEqual(insertion_sort(start), finish)

    def test_duplicates(self):
        start = [3, 3, 2, 1, 2]
        finish = [1, 2, 2, 3, 3]
        self.assertEqual(insertion_sort(start), finish)

if __name__ == '__main__':
    unittest.main()