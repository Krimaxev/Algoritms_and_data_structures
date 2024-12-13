import unittest
from lab_1.task_3.src.task3 import insertion_sort_three

class TestInsertionSort(unittest.TestCase):
    def test_sort_empty(self):
        start = []
        finish = []
        self.assertEqual(insertion_sort_three(start), finish)

    def test_sort_single_element(self):
        start = [1]
        finish = [1]
        self.assertEqual(insertion_sort_three(start), finish)

    def test_sort_sorted(self):
        start = [1, 2, 3, 4, 5]
        finish = [5, 4, 3, 2, 1]
        self.assertEqual(insertion_sort_three(start), finish)

    def test_sort_reverse_sorted(self):
        start = [5, 4, 3, 2, 1]
        finish = [5, 4, 3, 2, 1]
        self.assertEqual(insertion_sort_three(start), finish)

    def test_sort_unsorted(self):
        start = [3, 1, 4, 2, 5]
        finish = [5, 4, 3, 2, 1]
        self.assertEqual(insertion_sort_three(start), finish)

    def test_sort_with_duplicates(self):
        start = [3, 1, 2, 3, 3]
        finish = [3, 3, 3, 2, 1]
        self.assertEqual(insertion_sort_three(start), finish)

    def test_sort_negative_numbers(self):
        start = [-1, -3, 2, 1, 0]
        finish = [2, 1, 0, -1, -3]
        self.assertEqual(insertion_sort_three(start), finish)

    def test_sort_large_numbers(self):
        start = [1000, 500, 100, 0, 200]
        finish = [1000, 500, 200, 100, 0]
        self.assertEqual(insertion_sort_three(start), finish)

if __name__ == '__main__':
    unittest.main()
