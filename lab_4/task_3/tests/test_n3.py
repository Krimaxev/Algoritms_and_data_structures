import unittest
import resource
import time
from lab_4.task_3.src.main import bracket_sequence

class TestBracketSequence(unittest.TestCase):
    def test_correct_sequences(self):
        # Input data
        sequences = ["()", "[]", "([])", "()[]()"]
        expected = "ДА\nДА\nДА\nДА\n"

        # Given:
        result = bracket_sequence(sequences)

        # Then:
        self.assertEqual(result, expected)

    def test_incorrect_sequences(self):
        # Input data
        sequences = ["(", "[", "([)]", "())", "]["]
        expected = "НЕТ\nНЕТ\nНЕТ\nНЕТ\nНЕТ\n"

        # Given:
        result = bracket_sequence(sequences)

        # Then:
        self.assertEqual(result, expected)

    def test_mixed_sequences(self):
        # Input data
        sequences = ["([]", "[]()", "[)", "(([]))", "()"]
        expected = "НЕТ\nДА\nНЕТ\nДА\nДА\n"

        # Given:
        result = bracket_sequence(sequences)

        # Then:
        self.assertEqual(result, expected)

    def test_empty_string(self):
        # Input data
        sequences = ["", "()"]
        expected = "ДА\nДА\n"

        # Given:
        result = bracket_sequence(sequences)

        # Then:
        self.assertEqual(result, expected)

    def test_nested_structures(self):
        # Input data
        sequences = ["(((([[]]))))", "([[[[(((([]))))]]]])"]
        expected = "ДА\nДА\n"

        # Given:
        result = bracket_sequence(sequences)

        # Then:
        self.assertEqual(result, expected)

    def test_performance(self):
        # Input data
        sequences = ["(" * 50000 + ")" * 50000, "[" * 40000 + "]" * 40000]

        start_time = time.time()
        start_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

        # Given:
        result = bracket_sequence(sequences)

        end_time = time.time()
        end_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

        # Then:
        self.assertEqual(result, "ДА\nДА\n")
        print(f"Execution Time: {end_time - start_time} seconds")
        print(f"Memory Usage: {(end_memory - start_memory)/1024} KB")

if __name__ == "__main__":
    unittest.main()