import unittest
from lab_4.task_1.src.main import steck

class TestSteck(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(steck([]), [])

    def test_no_minus(self):
        self.assertEqual(steck(["123", "456"]), [])

    def test_valid_input(self):
        self.assertEqual(steck(["123","-", "abc", "456", "-"]), ["123", "456"])

    def test_mixed_input(self):
        self.assertEqual(steck(["1a2b-", "3c4d-", "5e6f"]), [])

    def test_non_list_input(self):
        self.assertEqual(steck("not a list"), [])


if __name__ == '__main__':
    unittest.main()