import unittest
from lab_3.task_3.src.main_3 import matreshka

class TestMatreshka(unittest.TestCase):

    def test_already_sorted(self):
        self.assertTrue(matreshka([1, 2, 3, 4, 5], 2))

    def test_reverse_sorted(self):
        self.assertTrue(matreshka([5, 4, 3, 2, 1], 2))

    def test_sortable(self):
        self.assertTrue(matreshka([3, 1, 2], 2))

    def test_unsortable(self):
        self.assertTrue(matreshka([3, 2, 1], 2))

    def test_sortable_2(self):
        self.assertFalse(matreshka([1, 3, 2, 4, 5], 2))

    def test_unsortable_2(self):
        self.assertFalse(matreshka([5, 4, 3, 2, 1], 3))

    def test_large_input(self):
        m = list(range(10, 0, -1))
        k = 2
        self.assertFalse(matreshka(m,k))

if __name__ == '__main__':
    unittest.main()