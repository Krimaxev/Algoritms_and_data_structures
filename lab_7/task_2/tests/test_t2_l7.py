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
        #input data
        n = 10
        #given
        expected_operations = 3
        expected_sequence = [1, 3, 9, 10]
        #then
        result_operations, result_sequence = primitive_calculator(n)
        self.assertEqual(result_operations, expected_operations)
        self.assertEqual(result_sequence, expected_sequence)

    def test_large_number(self):
        #input data
        n = 96234
        #given
        result_1 = 1
        result_2 = n
        #then
        _, result_sequence = primitive_calculator(n)
        self.assertEqual(result_sequence[0], result_1)
        self.assertEqual(result_sequence[-1], result_2)

    def test_one(self):
        #input data
        n = 1
        #given
        expected_operations = 0
        expected_sequence = [1]
        #then
        result_operations, result_sequence = primitive_calculator(n)
        self.assertEqual(result_operations, expected_operations)
        self.assertEqual(result_sequence, expected_sequence)

    def tearDown(self):
        end_time = time.time()
        end_memory = memory_usage()
        print(f"ЗАТРАТЫ ВРЕМЕНИ: {end_time - self.start_time} СЕКУНД(Ы)")
        print(f"ЗАТРАТЫ ПАМЯТИ: {(end_memory - self.start_memory) / 1024} Кб")

if __name__ == "__main__":
    unittest.main()