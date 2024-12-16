import unittest
from lab_3.task_2.src.main_2 import generate_worst_case
import resource
import time

class TestGenerateWorstCase(unittest.TestCase):

    def test_empty_input(self):
        # Given
        n = 0
        # When
        result = generate_worst_case(n)
        # Then
        self.assertEqual(result, [])

    def test_single_element_input(self):
        # Given
        n = 1
        # When
        result = generate_worst_case(n)
        # Then
        self.assertEqual(result, [1])

    def test_small_input(self):
        # Given
        n = 5
        # When
        result = generate_worst_case(n)
        # Then
        self.assertEqual(len(result), 5)
        self.assertTrue(all(1 <= x <= 5 for x in result))

    def test_larger_input(self):
        # Given
        n = 100
        # When
        result = generate_worst_case(n)
        # Then
        self.assertEqual(len(result), 100)
        self.assertTrue(all(1 <= x <= 100 for x in result))

    def test_all_elements_present(self):
        # Given
        n = 10
        # When
        result = generate_worst_case(n)
        # Then
        self.assertEqual(sorted(result), list(range(1, 11)))

    def test_memory_and_time_consumption(self):
        # Given
        n = 1000
        start_time = time.time()
        start_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        # When
        result = generate_worst_case(n)
        end_time = time.time()
        end_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        elapsed_time = end_time - start_time
        memory_usage = end_memory - start_memory
        # Then
        print(f"Execution time: {elapsed_time:.5f} seconds")
        print(f"Memory usage: {memory_usage} KB")
        self.assertEqual(len(result), n)
        self.assertEqual(sorted(result), list(range(1, n + 1)))

if __name__ == '__main__':
    unittest.main()