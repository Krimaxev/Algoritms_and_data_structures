import unittest
from lab_4.task_1.src.main import steck
import resource
import time

class TestSteck(unittest.TestCase):
    def test_empty_list(self):
        # Given
        input_data = []
        # When
        result = steck(input_data)
        # Then
        self.assertEqual(result, [])

    def test_no_minus(self):
        # Given
        input_data = ["123", "456"]
        # When
        result = steck(input_data)
        # Then
        self.assertEqual(result, [])

    def test_valid_input(self):
        # Given
        input_data = ["123", "-", "abc", "456", "-"]
        # When
        result = steck(input_data)
        # Then
        self.assertEqual(result, ["123", "456"])

    def test_mixed_input(self):
        # Given
        input_data = ["1a2b-", "3c4d-", "5e6f"]
        # When
        result = steck(input_data)
        # Then
        self.assertEqual(result, [])

    def test_non_list_input(self):
        # Given
        input_data = "not a list"
        # When
        result = steck(input_data)
        # Then
        self.assertEqual(result, [])

    def test_memory_and_time_consumption(self):
        # Given
        input_data = ["123", "-", "abc", "456", "-"] * 1000
        start_time = time.time()
        start_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        # When
        result = steck(input_data)
        # Then
        end_time = time.time()
        end_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        elapsed_time = end_time - start_time
        memory_usage = end_memory - start_memory
        print(f"Execution time: {elapsed_time:.5f} seconds")
        print(f"Memory usage: {(memory_usage)/1024} МB")
        self.assertEqual(result, ["123", "456"] * 1000)

if __name__ == '__main__':
    unittest.main()