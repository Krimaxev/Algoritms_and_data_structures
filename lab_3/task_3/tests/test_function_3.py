import unittest
from lab_3.task_3.src.main_3 import matreshka

class TestMatreshka(unittest.TestCase):
    def test_empty_array(self):
        self.assertTrue(matreshka([], 2, 0))

    def test_single_element(self):
        self.assertTrue(matreshka([5], 1, 1))

    def test_multiple_of_k(self):
        self.assertFalse(matreshka([1, 5, 2, 6, 3, 7, 4, 8], 2, 8))
        self.assertFalse(matreshka([1, 4, 7, 2, 5, 8, 3, 6], 4,8))

    def test_not_multiple_of_k(self):
        self.assertFalse(matreshka([1, 5, 2, 6, 3, 7, 4], 2, 7))
        self.assertFalse(matreshka([1, 5, 2, 6, 3, 7], 4, 6))

    def test_already_sorted(self):
      self.assertTrue(matreshka([1,2,3,4],2,4))

    def test_unsorted(self):
        self.assertFalse(matreshka([5,1,3,2],2,4))


if __name__ == '__main__':
    unittest.main()