import unittest
import resource
import time
from lab_7.task_2.src.main import primitive_calculator

def memory_usage():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

class TestPrimitiveCalculator(unittest.TestCase):
    def setUp(self):
        self.start_time = time.time()
        self.start_memory = memory_usage()

    def test_small_number(self):
        n = 10
        expected_operations = 3
        expected_sequence = [1, 3, 9, 10]
        result_operations, result_sequence = primitive_calculator(n)
        self.assertEqual(result_operations, expected_operations)
        self.assertEqual(result_sequence, expected_sequence)

    def test_large_number(self):
        n = 96234
        _, result_sequence = primitive_calculator(n)
        self.assertEqual(result_sequence[0], 1)  # Sequence should start from 1
        self.assertEqual(result_sequence[-1], n)  # Sequence should end with n

    def test_one(self):
        n = 1
        expected_operations = 0
        expected_sequence = [1]
        result_operations, result_sequence = primitive_calculator(n)
        self.assertEqual(result_operations, expected_operations)
        self.assertEqual(result_sequence, expected_sequence)

    def tearDown(self):
        end_time = time.time()
        end_memory = memory_usage()
        print(f"Execution Time: {end_time - self.start_time} seconds")
        print(f"Memory Usage: {(end_memory - self.start_memory) / 1024} KB")

if __name__ == "__main__":
    unittest.main()