import unittest
import resource
import time

from lab_7.task_5.src.main import longest_common_subsequence  # Предположим, функция находится в your_module.py


class TestLCS(unittest.TestCase):

    def test_small_case(self):
        # input data:
        self.a = [1, 2, 3]
        self.b = [2, 1, 3]
        self.c = [1, 3, 5]
        # given
        result = 2
        self.assertEqual(longest_common_subsequence(self.a, self.b, self.c), result)

    def test_large_case(self):
        start_time = time.time()
        usage_start = resource.getrusage(resource.RUSAGE_SELF)

        # input data:
        self.large_a = list(range(100))
        self.large_b = list(range(50, 150))
        self.large_c = list(range(75, 175))
        # given
        result = longest_common_subsequence(self.large_a, self.large_b, self.large_c)

        usage_end = resource.getrusage(resource.RUSAGE_SELF)
        end_time = time.time()

        memory_usage = usage_end.ru_maxrss - usage_start.ru_maxrss
        runtime = end_time - start_time

        print(f"ЗАТРАТЫ ВРЕМЕНИ: {runtime:.6f} СЕКУНД(Ы)")
        print(f"ЗАТРАТЫ ПАМЯТИ: {memory_usage/1024} Мб")

        self.assertEqual(result, 25)


if __name__ == "__main__":
    unittest.main()