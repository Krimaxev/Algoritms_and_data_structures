import unittest
from lab_1.task_6.src.task6 import bubble_sort

class TestBubbleSort(unittest.TestCase):
    def test_empty_list(self):
        start = []
        finish = []
        self.assertEqual(bubble_sort(start), finish)

    def test_single_element(self):
        start = [1]
        finish = [1]
        self.assertEqual(bubble_sort(start), finish)

    def test_sorted_list(self):
        start = [1, 2, 3]
        finish = [1, 2, 3]
        self.assertEqual(bubble_sort(start), finish)

    def test_unsorted_list(self):
        start = [3, 2, 1]
        finish = [1, 2, 3]
        self.assertEqual(bubble_sort(start), finish)

    def test_duplicates(self):
        start = [3, 1, 2, 1, 3]
        finish = [1, 1, 2, 3, 3]
        self.assertEqual(bubble_sort(start), finish)

if __name__ == "__main__":
    unittest.main()