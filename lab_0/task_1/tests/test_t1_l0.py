import unittest
import resource
import time
from lab_0.task_1.src.n1_1 import summ
from lab_0.task_1.src.n1_2 import easy_operation
from lab_0.task_1.src.n1_3 import summ_file
from lab_0.task_1.src.n1_4 import easy_operation_file

class TestOperations(unittest.TestCase):
    def test_summ(self):
        # Given
        input_data_1 = (2, 3)
        input_data_2 = (-1, 1)
        expected_1 = 5
        expected_2 = 0
        # When
        result_1 = summ(*input_data_1)
        result_2 = summ(*input_data_2)
        # Then
        self.assertEqual(result_1, expected_1)
        self.assertEqual(result_2, expected_2)

    def test_easy_operation(self):
        # Given
        input_data_1 = (2, 3)
        input_data_2 = (1, 4)
        expected_1 = 11
        expected_2 = 17
        # When
        result_1 = easy_operation(*input_data_1)
        result_2 = easy_operation(*input_data_2)
        # Then
        self.assertEqual(result_1, expected_1)
        self.assertEqual(result_2, expected_2)

    def test_summ_file(self):
        # Given
        input_data_1 = (5, 7)
        input_data_2 = (-3, 3)
        expected_1 = 12
        expected_2 = 0
        # When
        result_1 = summ_file(*input_data_1)
        result_2 = summ_file(*input_data_2)
        # Then
        self.assertEqual(result_1, expected_1)
        self.assertEqual(result_2, expected_2)

    def test_easy_operation_file(self):
        # Given
        input_data_1 = (2, 3)
        input_data_2 = (1, 4)
        expected_1 = 11
        expected_2 = 17
        # When
        result_1 = easy_operation_file(*input_data_1)
        result_2 = easy_operation_file(*input_data_2)
        # Then
        self.assertEqual(result_1, expected_1)
        self.assertEqual(result_2, expected_2)

    def test_memory_and_time_consumption(self):
        # Given
        input_data = (10**15, 10**15)
        start_time = time.time()
        start_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        # When
        result = summ(*input_data)
        end_time = time.time()
        end_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        elapsed_time = end_time - start_time
        memory_usage = end_memory - start_memory
        # Then
        print(f"Execution time: {elapsed_time:.5f} seconds.")
        print(f"Memory usage: {memory_usage} MB.")
        self.assertGreater(result, 0)

if __name__ == '__main__':
    unittest.main()