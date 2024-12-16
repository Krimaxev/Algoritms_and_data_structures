import unittest
import time
import resource
from lab_6.task_5.src.main import process_votes


class TestProcessVotes(unittest.TestCase):

    def test_basic_functionality(self):
        #input data
        lines = [
            "Alice 3",
            "Bob 2",
            "Alice 2",
            "Charlie 5",
            "Bob 1"
        ]
        #given
        expected = {'Alice': 5, 'Bob': 3, 'Charlie': 5}
        #then
        self.assertEqual(process_votes(lines), expected)

    def test_empty_input(self):
        #input data
        len_zero = []
        #given
        zero_dictionary = {}
        self.assertEqual(process_votes(len_zero), zero_dictionary)

    def test_performance(self):
        #input data
        lines = [f"Candidate{i} {i}" for i in range(1, 100001)]
        start_time = time.time()
        initial_mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        #then
        process_votes(lines)

        end_time = time.time()
        final_mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

        print(f"ЗАТРАТЫ ВРЕМЕНИ: {end_time - start_time} СЕКУНД(Ы)")
        print(f"ЗАТРАТЫ ПАМЯТИ: {(final_mem - initial_mem)//8//1024} Кб")


if __name__ == "__main__":
    unittest.main()