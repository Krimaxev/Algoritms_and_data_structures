import unittest
import resource
import time
from lab_5.task2.src.main import compute_tree_height

class TestComputeTreeHeight(unittest.TestCase):
    def test_example_1(self):
        # Input data
        nodes_count = 5
        parents = [4, -1, 4, 1, 1]
        expected_result = 3

        # Given:
        result = compute_tree_height(nodes_count, parents)

        # Then:
        self.assertEqual(result, expected_result)

    def test_example_2(self):
        # Input data
        nodes_count = 5
        parents = [-1, 0, 4, 0, 3]
        expected_result = 4

        # Given:
        result = compute_tree_height(nodes_count, parents)

        # Then:
        self.assertEqual(result, expected_result)

    def test_single_node(self):
        # Input data
        nodes_count = 1
        parents = [-1]
        expected_result = 1

        # Given:
        result = compute_tree_height(nodes_count, parents)

        # Then:
        self.assertEqual(result, expected_result)

    def test_linear_tree(self):
        # Input data
        nodes_count = 4
        parents = [-1, 0, 1, 2]
        expected_result = 4

        # Given:
        result = compute_tree_height(nodes_count, parents)

        # Then:
        self.assertEqual(result, expected_result)

    def test_star_tree(self):
        # Input data
        nodes_count = 5
        parents = [-1, 0, 0, 0, 0]
        expected_result = 2

        # Given:
        result = compute_tree_height(nodes_count, parents)

        # Then:
        self.assertEqual(result, expected_result)

    def test_performance(self):
        # Input data
        nodes_count = 100000
        parents = list(range(-1, nodes_count - 1))

        # Start tracking performance
        start_time = time.time()
        start_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

        # Given:
        result = compute_tree_height(nodes_count, parents)

        end_time = time.time()
        end_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

        # Then:
        self.assertTrue(result > 0)
        print(f"Execution Time: {end_time - start_time} seconds")
        print(f"Memory Usage: {end_memory - start_memory} KB")

if __name__ == "__main__":
    unittest.main()