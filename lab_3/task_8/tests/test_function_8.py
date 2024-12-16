import unittest
from lab_3.task_8.src.main_8 import closest_points
import resource
import time

class TestKClosestPoints(unittest.TestCase):
    def test_empty_points(self):
        # Given
        points = []
        k = 3
        # When
        result = closest_points(points, k)
        # Then
        self.assertEqual(result, [])

    def test_insufficient_points(self):
        # Given
        points = [(1, 2), (3, 4)]
        k = 5
        # When
        result = closest_points(points, k)
        # Then
        self.assertEqual(result, [(1, 2), (3, 4)])

    def test_some_points(self):
        # Given
        points = [(1, 2), (3, 4), (0, 0), (-1, -1)]
        k = 2
        # When
        result = closest_points(points, k)
        # Then
        self.assertEqual(result, [(0, 0), (-1, -1)])

    def test_all_points(self):
        # Given
        points = [(1, 2), (3, 4), (0, 0), (-1, -1)]
        k = 4
        # When
        result = closest_points(points, k)
        # Then
        self.assertEqual(result, [(0, 0), (-1, -1), (1, 2), (3, 4)])

    def test_invalid_point(self):
        # Given
        points = [(1, 2), (3)]  # Invalid point
        k = 2
        # Then
        with self.assertRaises(ValueError):
            # When
            closest_points(points, k)

    def test_memory_and_time_consumption(self):
        # Given
        points = [(x, x) for x in range(1000)]
        k = 3
        start_time = time.time()
        start_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        # When
        result = closest_points(points, k)
        end_time = time.time()
        end_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        elapsed_time = end_time - start_time
        memory_usage = end_memory - start_memory
        print(f"Execution time: {elapsed_time:.5f} seconds")
        print(f"Memory usage: {(memory_usage)/1024} MB")
        # Then
        self.assertEqual(len(result), k)

if __name__ == '__main__':
    unittest.main()