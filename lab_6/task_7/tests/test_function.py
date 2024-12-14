import time
import resource
import unittest
from lab_6.task_7.src.main import count_beautiful_pairs

class TestCountBeautifulPairs(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(count_beautiful_pairs(""), 0)

    def test_single_char(self):
        self.assertEqual(count_beautiful_pairs("a"), 0)

    def test_no_beautiful_pairs(self):
        self.assertEqual(count_beautiful_pairs("aaaa"), 0)

    def test_all_beautiful_pairs(self):
        self.assertEqual(count_beautiful_pairs("abab"), 3)

    def test_mixed_string(self):
        self.assertEqual(count_beautiful_pairs("abcabc"), 5)

    def test_performance(self):
        test_string = "a" * 10 ** 6 + "b" * 10 ** 6
        start_time = time.time()
        start_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        count_beautiful_pairs(test_string)
        end_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        end_time = time.time()
        print(f"Time: {end_time - start_time} seconds")
        print(f"Memory: {end_memory - start_memory} KB")



if __name__ == "__main__":
    unittest.main()