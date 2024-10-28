import unittest
from lab_2.task_6.src.main_t_6 import *

class TestMaxProfit(unittest.TestCase):

    def test_max_profit(self):
        self.assertEqual(Max_subarray([7, 1, 5, 3, 6, 4]), [1, 7, 6])
        self.assertEqual(Max_subarray([7, 6, 4, 3, 1]), [1, 7, 6])
        self.assertEqual(Max_subarray([]), [0, 0, 0])
        self.assertEqual(Max_subarray([1, 2, 3]), [1, 3, 2])
        self.assertEqual(Max_subarray([3, 2, 4, 1, 5]), [1, 5, 4])

if __name__ == '__main__':
    unittest.main()