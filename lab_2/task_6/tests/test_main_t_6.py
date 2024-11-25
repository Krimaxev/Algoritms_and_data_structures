import unittest
from lab_2.task_6.src.main_t_6 import max_subarray

class TestMaxProfit(unittest.TestCase):

    def test_max_profit(self):
        self.assertEqual(max_subarray([7, 1, 5, 3, 6, 4],[1,2,3,4,5,6]), [1, 6, 5, 2, 5])
        self.assertEqual(max_subarray([7, 6, 4, 3, 1],[10, 11, 12, 13, 14, 15]), [0, 0, 0, None, None])
        self.assertEqual(max_subarray([],[]), [0, 0, 0, None, None])
        self.assertEqual(max_subarray([1, 2, 3],[10, 11, 12]), [1, 3, 2, 10, 12])
        self.assertEqual(max_subarray([3, 2, 4, 1, 5], [21, 22, 23, 24, 25]), [1, 5, 4, 24, 25])

if __name__ == '__main__':
    unittest.main()