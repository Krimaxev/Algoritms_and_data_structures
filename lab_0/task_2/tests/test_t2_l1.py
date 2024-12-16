import unittest
import resource
import time
from lab_0.task_2.src.n2 import fibonacci

class TestFibonacci(unittest.TestCase):
    def test_fibonacci(self):
        # Given
        input_data_1 = 1
        input_data_2 = 6
        expected_result_1 = '1'
        expected_result_2 = '8'
        # When
        result_1 = fibonacci(input_data_1)
        result_2 = fibonacci(input_data_2)
        # Then
        self.assertEqual(result_1, expected_result_1)
        self.assertEqual(result_2, expected_result_2)
        self.assertEqual(fibonacci(2), '1')
        self.assertEqual(fibonacci(3), '2')
        self.assertEqual(fibonacci(4), '3')
        self.assertEqual(fibonacci(5), '5')

    def test_memory_and_time_consumption(self):
        # Given
        input_data = 1000
        start_time = time.time()
        start_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        # When
        result = fibonacci(input_data)
        end_time = time.time()
        end_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        elapsed_time = end_time - start_time
        memory_usage = end_memory - start_memory
        # Then
        print(f"Execution time: {elapsed_time:.5f} seconds.")
        print(f"Memory usage: {memory_usage} MB.")
        self.assertTrue(result.isdigit())

if __name__ == '__main__':
    unittest.main()