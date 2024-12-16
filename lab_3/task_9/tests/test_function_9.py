import unittest
from lab_3.task_9.src.main_9 import closest_pair
import resource
import time

class TestClosestPair(unittest.TestCase):
    def test_small_set(self):
        # Given
        points = [(1, 1), (2, 2), (3, 3)]
        # When
        result = closest_pair(points)
        # Then
        self.assertAlmostEqual(result, 1.41421356, places=7)

    def test_larger_set(self):
        # Given
        points = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (1.1, 1.1)]
        # When
        result = closest_pair(points)
        # Then
        self.assertAlmostEqual(result, 0.141421356, places=7)

    def test_empty_set(self):
        # Given
        points = []
        # When
        result = closest_pair(points)
        # Then
        self.assertEqual(result, float('inf'))

    def test_memory_and_time_consumption(self):
        # Given
        points = [(x, y) for x in range(100) for y in range(100)]
        start_time = time.time()
        start_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        # When
        result = closest_pair(points)
        end_time = time.time()
        end_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        # Then
        elapsed_time = end_time - start_time
        memory_usage = end_memory - start_memory
        print(f"Execution time: {elapsed_time:.5f} seconds")
        print(f"Memory usage: {memory_usage} KB")
        self.assertGreater(result, 0)

if __name__ == "__main__":
    unittest.main()