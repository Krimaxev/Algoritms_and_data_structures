
import unittest
import time
import resource
from lab_6.task_5.src.main import process_votes


class TestProcessVotes(unittest.TestCase):

    def test_basic_functionality(self):
        lines = [
            "Alice 3",
            "Bob 2",
            "Alice 2",
            "Charlie 5",
            "Bob 1"
        ]
        expected = {'Alice': 5, 'Bob': 3, 'Charlie': 5}
        self.assertEqual(process_votes(lines), expected)

    def test_empty_input(self):
        self.assertEqual(process_votes([]), {})

    def test_performance(self):
        lines = [f"Candidate{i} {i}" for i in range(1, 100001)]  # 100000 entries
        start_time = time.time()
        initial_mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

        process_votes(lines)

        end_time = time.time()
        final_mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

        print(f"Execution time: {end_time - start_time} seconds")
        print(f"Memory used: {(final_mem - initial_mem)//8//1024} КB")


if __name__ == "__main__":
    unittest.main()