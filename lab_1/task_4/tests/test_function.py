import unittest
from lab_1.task_4.src.task4 import line_find

class TestLineFind(unittest.TestCase):
    def test_no_occurrences(self):
        argue_1 = 10
        argue_2 = [1, 2, 3, 4, 5]
        result = "-1"
        self.assertEqual(line_find(argue_1, argue_2), result)

    def test_one_occurrence(self):
        argue_1 = 3
        argue_2 = [1, 2, 3, 4, 5]
        result = "2"
        self.assertEqual(line_find(argue_1, argue_2), result)

    def test_multiple_occurrences(self):
        argue_1 = 2
        argue_2 = [1, 2, 3, 2, 4, 2]
        result = "3\n1, 3, 5"
        self.assertEqual(line_find(argue_1, argue_2), result)


if __name__ == "__main__":
    unittest.main()