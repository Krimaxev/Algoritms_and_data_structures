import unittest
from lab_2.task_5.src.main_5 import majority

class TestMajority(unittest.TestCase):
    def test_majority_element_exists(self):
        self.assertEqual(majority([1, 2, 3, 2, 2]), 1)

    def test_majority_element_not_exists(self):
        self.assertEqual(majority([1, 2, 3, 4]), 0)

    def test_no_elements(self):
        self.assertEqual(majority([]), 0)

    def test_all_same_elements(self):
        self.assertEqual(majority([1, 1, 1, 1]), 1)

    def test_multiple_elements_majority(self):
        self.assertEqual(majority([1, 1, 2, 2, 2]), 1)

if __name__ == '__main__':
    unittest.main()