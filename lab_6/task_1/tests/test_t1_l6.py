import unittest
from lab_6.task_1.src.main import process_operations
import resource
import time

class TestProcessOperations(unittest.TestCase):
    def test_operations(self):
        # Input data:
        operations = ["A 2", "A 5", "A 3", "? 2", "? 4", "A 2", "D 2", "? 2"]
        # Given:
        expected = ["Y", "N", "N"]
        # Then:
        self.assertEqual(process_operations(operations), expected)

    def test_empty_operations(self):
        # Input data:
        operations = []
        # Given:
        expected = []
        # Then:
        self.assertEqual(process_operations(operations), expected)

    def test_only_queries(self):
        # Input data:
        operations = ["? 1", "? 2", "? 3"]
        # Given:
        expected = ["N", "N", "N"]
        # Then:
        self.assertEqual(process_operations(operations), expected)

    def test_performance(self):
        # Input data:
        operations = ["A " + str(i) for i in range(100000)] + ["? " + str(i) for i in range(100000)]
        start_time = time.time()
        start_mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        process_operations(operations)
        end_time = time.time()
        end_mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        # Then:
        print(f"Execution Time: {end_time - start_time} seconds")
        print(f"Memory Usage: {end_mem - start_mem} KB")

if __name__ == '__main__':
    unittest.main()