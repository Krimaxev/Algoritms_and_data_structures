import unittest
from lab_2.task_3.src.main_3 import *
class TestInverseFunction(unittest.TestCase):

    def test_no_inversions(self):
        self.assertEqual(Inverse([1, 2, 3]), 0)

    def test_some_inversions(self):
        self.assertEqual(Inverse([3, 2, 1]), 3)
        self.assertEqual(Inverse([2, 4, 1, 3]), 3)

    def test_empty_list(self):
        self.assertEqual(Inverse([]), 0)

    def test_single_element(self):
        self.assertEqual(Inverse([1]), 0)


if __name__ == '__main__':
    unittest.main()