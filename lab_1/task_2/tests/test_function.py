import unittest

from lab_1.task_2.src.task2 import insertion_sort_two

class TestInsertionSort(unittest.TestCase):

    def test_empty_list(self):
        start = []
        finish = []
        self.assertEqual(insertion_sort_two(start), finish)

    def test_single_element_list(self):
        start = [42]
        finish = [0]
        self.assertEqual(insertion_sort_two(start), finish)  # The only index is 0

    def test_sorted_list(self):
        start = [1, 2, 3, 4, 5]
        finish = [0, 1, 2, 3, 4]
        self.assertEqual(insertion_sort_two(start), finish)

    def test_reverse_sorted_list(self):
        start = [5, 4, 3, 2, 1]
        finish = [0, 0, 0, 0, 0]
        self.assertEqual(insertion_sort_two(start), finish)

    def test_unsorted_list(self):
        start = [3, 1, 4, 2]
        finish = [0, 0, 2, 1]
        self.assertEqual(insertion_sort_two(start), finish)

    def test_duplicates(self):
        start = [2, 2, 1]
        finish = [0, 0, 0]
        self.assertEqual(insertion_sort_two(start), finish)


if __name__ == '__main__':
    unittest.main()