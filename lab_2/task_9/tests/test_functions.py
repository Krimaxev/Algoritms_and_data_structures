import unittest
from lab_2.task_9.src.Multiply import *
from lab_2.task_9.src.Strassen import *

class TestMatrixMultiplication(unittest.TestCase):

    def test_multiply_2x2(self):
        n = 2
        X = [[1, 2], [3, 4]]
        Y = [[5, 6], [7, 8]]
        expected_result = [[15, 17], [19, 21]]
        self.assertEqual(multiply(n, X, Y), expected_result)

    def test_multiply_3x3(self):
        n = 3
        X = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        Y = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
        expected_result = [[24, 21, 18], [33, 30, 27], [42, 39, 36]]
        self.assertEqual(multiply(n, X, Y), expected_result)

    def test_strassen_2x2(self):
        A = [[1, 2], [3, 4]]
        B = [[5, 6], [7, 8]]
        expected_result = [[19, 22], [43, 50]]
        self.assertEqual(strassen(A, B), expected_result)

if __name__ == '__main__':
    unittest.main()