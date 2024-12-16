import unittest
from lab_2.task_5.src.main_5 import majority
import resource
import time

class TestMajority(unittest.TestCase):
    def test_majority_element_exists(self):
        # Given
        input_data = [1, 2, 3, 2, 2]
        expected_result = 1
        # When
        result = majority(input_data)
        # Then
        self.assertEqual(result, expected_result)

    def test_majority_element_not_exists(self):
        # Given
        input_data = [1, 2, 3, 4]
        expected_result = 0
        # When
        result = majority(input_data)
        # Then
        self.assertEqual(result, expected_result)

    def test_no_elements(self):
        # Given
        input_data = []
        expected_result = 0
        # When
        result = majority(input_data)
        # Then
        self.assertEqual(result, expected_result)

    def test_all_same_elements(self):
        # Given
        input_data = [1, 1, 1, 1]
        expected_result = 1
        # When
        result = majority(input_data)
        # Then
        self.assertEqual(result, expected_result)

    def test_multiple_elements_majority(self):
        # Given
        input_data = [1, 1, 2, 2, 2]
        expected_result = 1
        # When
        result = majority(input_data)
        # Then
        self.assertEqual(result, expected_result)

    def test_memory_and_time_consumption(self):
        # Given
        input_data = [1] * 10000000 + [2] * 5000000
        start_time = time.time()
        start_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        # When
        result = majority(input_data)
        end_time = time.time()
        end_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        elapsed_time = end_time - start_time
        memory_usage = end_memory - start_memory
        # Then
        print(f"Execution time: {elapsed_time:.5f} seconds")
        print(f"Memory usage: {memory_usage} MB")
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()