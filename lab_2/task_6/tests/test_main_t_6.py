import unittest
from lab_2.task_6.src.main_t_6 import max_subarray
import resource
import time


class TestMaxProfit(unittest.TestCase):

    def test_max_profit(self):
        # Test case 1
        # Given
        prices = [7, 1, 5, 3, 6, 4]
        days = [1, 2, 3, 4, 5, 6]
        expected = [1, 6, 5, 2, 5]
        # When
        result = max_subarray(prices, days)
        # Then
        self.assertEqual(result, expected)

        # Test case 2
        prices = [7, 6, 4, 3, 1]
        days = [10, 11, 12, 13, 14, 15]
        expected = [0, 0, 0, None, None]
        self.assertEqual(max_subarray(prices, days), expected)

        # Test case 3
        prices = []
        days = []
        expected = [0, 0, 0, None, None]
        self.assertEqual(max_subarray(prices, days), expected)

        # Test case 4
        prices = [1, 2, 3]
        days = [10, 11, 12]
        expected = [1, 3, 2, 10, 12]
        self.assertEqual(max_subarray(prices, days), expected)

        # Test case 5
        prices = [3, 2, 4, 1, 5]
        days = [21, 22, 23, 24, 25]
        expected = [1, 5, 4, 24, 25]
        self.assertEqual(max_subarray(prices, days), expected)

    def test_memory_and_time_consumption(self):
        # Given
        prices = [x for x in range(1000000)]
        days = [x for x in range(1000000)]
        start_time = time.time()
        start_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        # When
        result = max_subarray(prices, days)
        end_time = time.time()
        end_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        elapsed_time = end_time - start_time
        memory_usage = end_memory - start_memory
        # Then
        print(f"Execution time: {elapsed_time:.5f} seconds")
        print(f"Memory usage: {(memory_usage)/2**10} KB")
        self.assertIsNotNone(result)


if __name__ == '__main__':
    unittest.main()