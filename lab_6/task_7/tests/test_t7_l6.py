import time
import resource
import unittest
from lab_6.task_7.src.main import count_beautiful_pairs

class TestCountBeautifulPairs(unittest.TestCase):
    def test_empty_string(self):
        #input data
        test_string = ""
        #given
        result = 0
        #then
        self.assertEqual(count_beautiful_pairs(test_string), result)

    def test_single_char(self):
        # input data
        test_string = ""
        # given
        result = 0
        # then
        self.assertEqual(count_beautiful_pairs(test_string), result)

    def test_no_beautiful_pairs(self):
        # input data
        test_string = "aaaa"
        # given
        result = 0
        # then
        self.assertEqual(count_beautiful_pairs(test_string), result)

    def test_all_beautiful_pairs(self):
        # input data
        test_string = "abab"
        # given
        result = 3
        # then
        self.assertEqual(count_beautiful_pairs(test_string), result)

    def test_mixed_string(self):
        # input data
        test_string = "abcabc"
        # given
        result = 5
        # then
        self.assertEqual(count_beautiful_pairs(test_string), result)

    def test_performance(self):
        # input data
        test_string = "a" * 10 ** 6 + "b" * 10 ** 6
        # then
        start_time = time.time()
        start_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        count_beautiful_pairs(test_string)
        end_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        end_time = time.time()
        print(f"ЗАТРАТЫ ВРЕМЕНИ: {end_time - start_time} СЕКУНД(Ы)")
        print(f"ЗАТРАТЫ ПАМЯТИ: {end_memory - start_memory} Кб")



if __name__ == "__main__":
    unittest.main()