import unittest
import resource
from time import time


from lab_7.task_3.src.main import levenshtein_distance_and_path


class TestLevenshtein(unittest.TestCase):

    def test_distance(self):
        cases = [
            ("kitten", "sitting", (3, ['change k s', 'change e i', 'add n'])),
            ("flaw", "lawn", (2, ['del f', 'add a'])),
            ("intention", "execution", (5, ['change i e', 'change n x', 'del t', 'change n c', 'add u'])),
            ("abc", "abc", (0, [])),
            ("", "abc", (3, ["add a", "add b", "add c"])),
            ("abc", "", (3, ["del a", "del b", "del c"]))
        ]

        for s1, s2, expected in cases:
            with self.subTest(s1=s1, s2=s2):
                distance, operations = levenshtein_distance_and_path(s1, s2)
                self.assertEqual((distance, operations[:len(expected[1])]), expected)

    def test_performance(self):
        s1 = "a" * 1000
        s2 = "b" * 1000

        # Измерение времени и памяти
        start_time = time()
        start_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

        levenshtein_distance_and_path(s1, s2)

        end_time = time()
        end_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

        elapsed_time = end_time - start_time
        used_memory = ((end_memory - start_memory) / 1024) /1024

        print(f"Elapsed time: {elapsed_time:.4f} seconds")
        print(f"Memory used: {used_memory:.4f} КB")

        self.assertLess(elapsed_time, 5)
        self.assertLess(used_memory, 256)


if __name__ == "__main__":
    unittest.main()