import unittest
import resource
import time
from lab_7.task_1.src.main import *


class TestMinChange(unittest.TestCase):
    def test_case_1(self):
        #input data
        coin = [1, 3, 4]
        total = 6
        #given
        num_coins =2
        #then
        self.assertEqual(min_change(coin, total), num_coins)

    def test_case_2(self):
        # input data
        coin = [1, 2, 5]
        total = 11
        # given
        num_coins = 3
        # then
        self.assertEqual(min_change(coin, total), num_coins)

    def test_case_3(self):
        # input data
        coin = [2]
        total = 3
        # given
        res_of_change = float('inf') - 1
        # then
        self.assertEqual(min_change(coin, total), res_of_change)

    def test_case_4(self):
        # input data
        coin = [1, 2, 3]
        total = 0
        # given
        num_coins = 0
        # then
        self.assertEqual(min_change(coin, total), num_coins)

    def test_case_5(self):
        # input data
        coin = [5, 10, 25]
        total = 30
        # given
        num_coins = 2
        # then
        self.assertEqual(min_change(coin, total), num_coins)

    def test_time_memory(self):
        # input data
        coins = [1, 3, 4]
        total = 6
        # then
        time_start = time.perf_counter()
        start_mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

        time_elapsed = (time.perf_counter() - time_start)

        print("Result:", min_change(coins, total))
        end_mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss  # Память после вызова
        end_time = time.time()

        print(f"ЗАТРАТЫ ВРЕМЕНИ: {time_elapsed} СЕКУНД(Ы)")
        print(f"ЗАТРАТЫ ПАМЯТИ: {end_mem - start_mem} Кб")


if __name__ == "__main__":
    unittest.main()