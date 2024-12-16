import unittest
import resource
import time
from lab_0.task_3.src.n3 import last_number_fibonacci

class TestLastNumberFibonacci(unittest.TestCase):
    def test_last_number_fibonacci(self):
        # Given
        input_data_1 = 0
        input_data_2 = 1
        input_data_3 = 10
        input_data_4 = 20
        expected_result_1 = 0
        expected_result_2 = 1
        expected_result_3 = 5
        expected_result_4 = 5
        # When and Then
        self.assertEqual(last_number_fibonacci(input_data_1), expected_result_1)
        self.assertEqual(last_number_fibonacci(input_data_2), expected_result_2)
        self.assertEqual(last_number_fibonacci(2), 1)
        self.assertEqual(last_number_fibonacci(3), 2)
        self.assertEqual(last_number_fibonacci(4), 3)
        self.assertEqual(last_number_fibonacci(5), 5)
        self.assertEqual(last_number_fibonacci(input_data_3), expected_result_3)
        self.assertEqual(last_number_fibonacci(input_data_4), expected_result_4)

    def test_memory_and_time_consumption(self):
        # Given
        input_data = 10000000
        start_time = time.time()
        start_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        # When
        result = last_number_fibonacci(input_data)
        end_time = time.time()
        end_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        elapsed_time = end_time - start_time
        memory_usage = end_memory - start_memory
        # Then
        print(f"Execution time: {elapsed_time:.5f} seconds.")
        print(f"Memory usage: {memory_usage} MB.")

        self.assertGreaterEqual(result, 0)
        self.assertLess(result, 10)

if __name__ == '__main__':
    unittest.main()