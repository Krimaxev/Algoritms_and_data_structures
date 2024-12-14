import unittest
from lab_6.task_1.src.main import process_operations

class TestProcessOperations(unittest.TestCase):
    def test_operations(self):
        operations = ["A 2", "A 5", "A 3", "? 2", "? 4", "A 2", "D 2", "? 2"]
        expected = ["Y", "N", "N"]
        self.assertEqual(process_operations(operations), expected)

    def test_empty_operations(self):
        operations = []
        expected = []
        self.assertEqual(process_operations(operations), expected)

    def test_only_queries(self):
        operations = ["? 1", "? 2", "? 3"]
        expected = ["N", "N", "N"]
        self.assertEqual(process_operations(operations), expected)

if __name__ == '__main__':
    unittest.main()