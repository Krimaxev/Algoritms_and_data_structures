import unittest
import resource
import time
from lab_4.task_5.src.main import process_stack

class TestProcessStack(unittest.TestCase):

    def test_push_max_pop(self):
        # Input data
        commands = ["push 5", "push 1", "push 10", "max", "pop", "max"]
        expected = ['10', '5']

        # Given:
        result = process_stack(commands)

        # Then:
        self.assertEqual(result, expected)

    def test_only_push_and_max(self):
        # Input data
        commands = ["push 3", "push 7", "push 2", "max"]
        expected = ['7']

        # Given:
        result = process_stack(commands)

        # Then:
        self.assertEqual(result, expected)

    def test_pop_until_empty(self):
        # Input data
        commands = ["push 4", "pop", "pop"]
        expected = []

        # Given:
        result = process_stack(commands)

        # Then:
        self.assertEqual(result, expected)

    def test_no_commands(self):
        # Input data
        commands = []
        expected = []

        # Given:
        result = process_stack(commands)

        # Then:
        self.assertEqual(result, expected)

    def test_only_max_command(self):
        # Input data
        commands = ["max"]
        expected = []

        # Given:
        result = process_stack(commands)

        # Then:
        self.assertEqual(result, expected)

    def test_performance(self):
        # Input data
        commands = ["push " + str(i) for i in range(1, 100001)] + ["max", "pop"] * 50000

        start_time = time.time()
        start_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

        # Given:
        result = process_stack(commands)

        end_time = time.time()
        end_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

        # Then:
        self.assertEqual(len(result), 50000)
        print(f"Execution Time: {end_time - start_time} seconds")
        print(f"Memory Usage: {(end_memory - start_memory)/1024} KB")

if __name__ == "__main__":
    unittest.main()