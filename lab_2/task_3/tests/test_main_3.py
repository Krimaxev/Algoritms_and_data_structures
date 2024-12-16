import unittest
from lab_2.task_3.src.main_3 import inverse
import resource
import time

class TestInverseFunction(unittest.TestCase):

    def test_no_inversions(self):
        # Given
        input_data = [1, 2, 3]
        expected_result = 0
        # When
        result = inverse(input_data)
        # Then
        self.assertEqual(result, expected_result)

    def test_some_inversions(self):
        # Given
        input_data1 = [3, 2, 1]
        expected_result1 = 3
        input_data2 = [2, 4, 1, 3]
        expected_result2 = 3
        # When
        result1 = inverse(input_data1)
        result2 = inverse(input_data2)
        # Then
        self.assertEqual(result1, expected_result1)
        self.assertEqual(result2, expected_result2)

    def test_empty_list(self):
        # Given
        input_data = []
        expected_result = 0
        # When
        result = inverse(input_data)
        # Then
        self.assertEqual(result, expected_result)

    def test_single_element(self):
        # Given
        input_data = [1]
        expected_result = 0
        # When
        result = inverse(input_data)
        # Then
        self.assertEqual(result, expected_result)

    def test_memory_and_time_consumption(self):
        # Given
        input_data = [i for i in range(1000, 0, -1)]  # Reverse sorted data
        start_time = time.time()
        start_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        # When
        result = inverse(input_data)
        end_time = time.time()
        end_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        elapsed_time = end_time - start_time
        memory_usage = end_memory - start_memory
        # Then
        print(f"Execution time: {elapsed_time:.5f} seconds")
        print(f"Memory usage: {memory_usage} MB")
        self.assertEqual(result, 499500)  # Formula for inversions in reverse sorted list: n * (n-1) / 2

if __name__ == '__main__':
    unittest.main()