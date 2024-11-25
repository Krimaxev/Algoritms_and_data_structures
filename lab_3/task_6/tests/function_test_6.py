import unittest
from lab_3.task_6.scr.main_6 import sort_z

class TestSortZ(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(sort_z("../txtf/test_input"), 3)

    def test_case2(self):
        self.assertEqual(sort_z("../txtf/test_input2"), 4)


if __name__ == '__main__':
    unittest.main()