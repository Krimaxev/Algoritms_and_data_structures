import unittest
from lab_3.task_6.scr.main_6 import sort_z

class TestSortZ(unittest.TestCase):
    def test_empty_lists(self):
        self.assertEqual(sort_z([], []), 0)
        self.assertEqual(sort_z([1,2],[]), 0)
        self.assertEqual(sort_z([],[1,2]), 0)

    def test_small_lists(self):
        self.assertTrue(sort_z([1, 2], [3, 4]), 11)
        self.assertTrue(sort_z([2,3],[4,5]), 14)

    def test_larger_lists(self):
        self.assertTrue(sort_z([1,2,3],[4,5,6]), 27)


if __name__ == '__main__':
    unittest.main()