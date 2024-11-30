import unittest
from lab_3.task_9.src.main_9 import closest_pair

class TestClosestPair(unittest.TestCase):
    def test_small_set(self):
        points = [(1,1),(2,2),(3,3)]
        self.assertAlmostEqual(closest_pair(points), 1.41421356, places=7)

    def test_larger_set(self):
        points = [(1,1),(2,2),(3,3),(4,4),(5,5),(1.1,1.1)]
        self.assertAlmostEqual(closest_pair(points), 0.141421356, places=7)

    def test_empty_set(self):
        self.assertEqual(closest_pair([]),float('inf'))


if __name__ == "__main__":
    unittest.main()