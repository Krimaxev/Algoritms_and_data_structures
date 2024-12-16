import unittest
from lab_2.task_9.src.Multiply import *
from lab_2.task_9.src.Strassen import *
import resource
import time

class TestMatrixMultiplication(unittest.TestCase):

    def test_multiply_2x2(self):
        # Given
        n = 2
        X = [[1, 2], [3, 4]]
        Y = [[5, 6], [7, 8]]
        expected_result = [[15, 17], [19, 21]]
        # When
        result = multiply(n, X, Y)
        # Then
        self.assertEqual(result, expected_result)

    def test_multiply_3x3(self):
        # Given
        n = 3
        X = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        Y = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
        expected_result = [[24, 21, 18], [33, 30, 27], [42, 39, 36]]
        # When
        result = multiply(n, X, Y)
        # Then
        self.assertEqual(result, expected_result)

    def test_strassen_2x2(self):
        # Given
        A = [[1, 2], [3, 4]]
        B = [[5, 6], [7, 8]]
        expected_result = [[19, 22], [43, 50]]
        # When
        result = strassen(A, B)
        # Then
        self.assertEqual(result, expected_result)

    def test_memory_and_time_consumption_multiply(self):
        # Given
        n = 50
        X = [[1 for _ in range(n)] for _ in range(n)]
        Y = [[1 for _ in range(n)] for _ in range(n)]
        start_time = time.time()
        start_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        # When
        result = multiply(n, X, Y)
        end_time = time.time()
        end_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        elapsed_time = end_time - start_time
        memory_usage = end_memory - start_memory
        # Then
        print(f"[Multiply] Execution time: {elapsed_time:.5f} seconds")
        print(f"[Multiply] Memory usage: {memory_usage} KB")
        self.assertEqual(len(result), n)

    def test_memory_and_time_consumption_strassen(self):
        # Given
        n = 16
        A = [[1 for _ in range(n)] for _ in range(n)]
        B = [[1 for _ in range(n)] for _ in range(n)]
        start_time = time.time()
        start_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        # When
        result = strassen(A, B)
        end_time = time.time()
        end_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        elapsed_time = end_time - start_time
        memory_usage = end_memory - start_memory
        # Then
        print(f"[Strassen] Execution time: {elapsed_time:.5f} seconds")
        print(f"[Strassen] Memory usage: {memory_usage} KB")
        self.assertEqual(len(result), n)

if __name__ == '__main__':
    unittest.main()