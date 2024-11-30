import unittest
from lab_4.task_5.src.main import process_stack

class TestProcessStack(unittest.TestCase):

    def test_push_max_pop(self):
        commands = ["push 5", "push 1", "push 10", "max", "pop", "max"]
        expected = ['10', '5']
        self.assertEqual(process_stack(commands), expected)

    def test_only_push_and_max(self):
        commands = ["push 3", "push 7", "push 2", "max"]
        expected = ['7']
        self.assertEqual(process_stack(commands), expected)

    def test_pop_until_empty(self):
        commands = ["push 4", "pop", "pop"]
        expected = []
        self.assertEqual(process_stack(commands), expected)

    def test_no_commands(self):
        commands = []
        expected = []
        self.assertEqual(process_stack(commands), expected)

    def test_only_max_command(self):
        commands = ["max"]
        expected = []
        self.assertEqual(process_stack(commands), expected)