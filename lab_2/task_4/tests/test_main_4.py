import unittest
from lab_2.task_4.src.main_4 import binary_search

class TestBinarySearch(unittest.TestCase):
    def test_found(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 3), 2)

    def test_not_found(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 6), -1)

    def test_empty_list(self):
        self.assertEqual(binary_search([], 1), -1)

    def test_first_element(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 1), 0)

    def test_last_element(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 5), 4)


if __name__ == '__main__':
    unittest.main()