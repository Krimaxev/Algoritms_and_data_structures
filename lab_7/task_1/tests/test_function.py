import unittest
import resource
import time
from lab_7.task_1.src.main import *


class TestMinChange(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(min_change([1, 3, 4], 6), 2)  # 3+3 = 6

    def test_case_2(self):
        self.assertEqual(min_change([1, 2, 5], 11), 3)  # 5+5+1 = 11

    def test_case_3(self):
        self.assertEqual(min_change([2], 3), float('inf') - 1)  # Невозможно разменять

    def test_case_4(self):
        self.assertEqual(min_change([1, 2, 3], 0), 0)  # Нечего разменивать

    def test_case_5(self):
        self.assertEqual(min_change([5, 10, 25], 30), 2)  # 25+5 = 30

    def test_time_memory(self):
        coins = [1, 3, 4]
        total = 6

        start_time = time.time()
        start_mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss  # Память до вызова

        print("Result:", min_change(coins, total))
        end_mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss  # Память после вызова
        end_time = time.time()

        print(f"ЗАТРАТЫ ВРЕМЕНИ: {end_time - start_time} СЕКУНД(Ы)")
        print(f"ЗАТРАТЫ ПАМЯТИ: {end_mem - start_mem} Кб")


if __name__ == "__main__":
    unittest.main()