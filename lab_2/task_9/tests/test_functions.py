import unittest
from lab_2.task_9.src.Multiply import *
from lab_2.task_9.src.Strassen import *

class TestMatrixMultiplication(unittest.TestCase):

    def test_multiply_2x2(self):
        n = 2
        X = [[1, 2], [3, 4]]
        Y = [[5, 6], [7, 8]]
        expected_result = [[19, 22], [43, 50]]
        self.assertEqual(multiply(n, X, Y), expected_result)

    def test_multiply_3x3(self):
        n = 3
        X = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        Y = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
        expected_result = [[30, 24, 18], [84, 69, 54], [138, 114, 90]]
        self.assertEqual(multiply(n, X, Y), expected_result)

class TestStrassen(unittest.TestCase):

    def test_strassen_2x2(self):
        A = [[1, 2], [3, 4]]
        B = [[5, 6], [7, 8]]
        expected_result = [[19, 22], [43, 50]]
        self.assertEqual(strassen(A, B), expected_result)

    def test_strassen_4x4(self):
        A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        B = [[17, 18, 19, 20], [21, 22, 23, 24], [25, 26, 27, 28], [29, 30, 31, 32]]
        expected_result = [[238, 254, 270, 286], [586, 622, 658, 694], [934, 990, 1046, 1102], [1282, 1358, 1434, 1510]]
        self.assertEqual(strassen(A, B), expected_result)




if __name__ == '__main__':
    unittest.main()