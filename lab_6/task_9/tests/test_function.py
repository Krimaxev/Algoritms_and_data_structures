import time
import resource
import unittest
from lab_6.task_9.src.main import hash_killer

class TestHashKiller(unittest.TestCase):
    def test_small_input(self):
        # Given: small input value of 5
        # Then: function should generate 5 unique strings
        result = hash_killer(5)
        # Result: Check the correctness of output
        expected = "aaaaaa\naaaaab\naaaaac\naaaaad\naaaaae\n"
        self.assertEqual(result, expected)

    def test_large_input(self):
        # Given: larger input value of 53
        # Then: function should generate 53 unique strings
        result = hash_killer(53)
        # Result: Validate structure and uniqueness of generated string
        lines = result.strip().split('\n')
        self.assertEqual(len(lines), 53)
        self.assertEqual(len(set(lines)), 53)  # Ensure all strings are unique

    def test_no_input(self):
        # Given: input value 0
        # Then: function should return an empty string
        result = hash_killer(0)
        # Result: Output should be empty
        self.assertEqual(result, '')

    def test_performance(self):
        # Given: input size
        value = 1000

        # Then: measure start time and memory
        start_time = time.time()
        start_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

        # Perform operation
        hash_killer(value)

        # Measure end time and memory
        end_time = time.time()
        end_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

        # Result: вывод метрик
        print(f"Execution time: {end_time - start_time:.6f} seconds")
        print(f"Memory used: {(end_memory - start_memory)//1024} MB")

if __name__ == '__main__':
    unittest.main()
