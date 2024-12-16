import time
import resource
import unittest
from lab_6.task_9.src.main import hash_killer

class TestHashKiller(unittest.TestCase):
    def test_small_input(self):
        # Given:
        # Then:
        result = hash_killer(5)
        # Result:
        expected = "aaaaaa\naaaaab\naaaaac\naaaaad\naaaaae\n"
        self.assertEqual(result, expected)

    def test_large_input(self):
        # Given:
        # Then:
        result = hash_killer(53)
        # Result:
        lines = result.strip().split('\n')
        self.assertEqual(len(lines), 53)
        self.assertEqual(len(set(lines)), 53)  #

    def test_no_input(self):
        # Given:
        # Then:
        result = hash_killer(0)
        # Result:
        self.assertEqual(result, '')

    def test_performance(self):
        # Given:
        value = 1000

        # Then:
        start_time = time.time()
        start_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

        hash_killer(value)

        end_time = time.time()
        end_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

        # Result:
        print(f"Execution time: {end_time - start_time:.6f} seconds")
        print(f"Memory used: {(end_memory - start_memory)//1024} MB")

if __name__ == '__main__':
    unittest.main()
