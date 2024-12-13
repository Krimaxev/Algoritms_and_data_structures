import unittest
from lab_0.task_1.src.n1_1 import summ
from lab_0.task_1.src.n1_2 import easy_operation
from lab_0.task_1.src.n1_3 import summ_file
from lab_0.task_1.src.n1_4 import easy_operation_file

class TestOperations(unittest.TestCase):
    def test_summ(self):
        self.assertEqual(summ(2, 3), 5)
        self.assertEqual(summ(-1, 1), 0)

    def test_easy_operation(self):
        self.assertEqual(easy_operation(2, 3), 11)  # 2 + 3^2 = 2 + 9
        self.assertEqual(easy_operation(1, 4), 17)  # 1 + 4^2 = 1 + 16

    def test_summ_file(self):
        self.assertEqual(summ_file(5, 7), 12)
        self.assertEqual(summ_file(-3, 3), 0)

    def test_easy_operation_file(self):
        self.assertEqual(easy_operation_file(2, 3), 11)  # 2 + 3^2 = 2 + 9
        self.assertEqual(easy_operation_file(1, 4), 17)  # 1 + 4^2 = 1 + 16

if __name__ == '__main__':
    unittest.main()