import unittest
from lab_3.task_8.src.main_8 import closest_points

class TestKClosestPoints(unittest.TestCase):
    def test_empty_points(self):
        self.assertEqual(closest_points([], 3), [])

    def test_insufficient_points(self):
        self.assertEqual(closest_points([(1, 2), (3, 4)], 5), [(1, 2), (3, 4)])

    def test_some_points(self):
        self.assertEqual(closest_points([(1, 2), (3, 4), (0, 0), (-1, -1)], 2), [(0, 0), (-1, -1)])

    def test_all_points(self):
        self.assertEqual(closest_points([(1, 2), (3, 4), (0, 0), (-1, -1)], 4), [(0, 0), (-1, -1), (1, 2), (3, 4)])

    def test_invalid_point(self):
        with self.assertRaises(ValueError):
            closest_points([(1, 2), (3)], 2)


if __name__ == '__main__':
    unittest.main()