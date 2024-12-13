import unittest
from lab_5.task2.src.main import compute_tree_height

class TestComputeTreeHeight(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(compute_tree_height(5, [4, -1, 4, 1, 1]), 3)

    def test_example_2(self):
        self.assertEqual(compute_tree_height(5, [-1, 0, 4, 0, 3]), 4)

    def test_single_node(self):
        self.assertEqual(compute_tree_height(1, [-1]), 1)

    def test_linear_tree(self):
        self.assertEqual(compute_tree_height(4, [-1, 0, 1, 2]), 4)

    def test_star_tree(self):
        self.assertEqual(compute_tree_height(5, [-1, 0, 0, 0, 0]), 2)

if __name__ == "__main__":
    unittest.main()