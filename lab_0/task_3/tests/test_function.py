import unittest
from lab_0.task_3.src.n3 import last_number_fibonacci

class TestLastNumberFibonacci(unittest.TestCase):
    def test_last_number_fibonacci(self):
        self.assertEqual(last_number_fibonacci(0), 0)
        self.assertEqual(last_number_fibonacci(1), 1)
        self.assertEqual(last_number_fibonacci(2), 1)
        self.assertEqual(last_number_fibonacci(3), 2)
        self.assertEqual(last_number_fibonacci(4), 3)
        self.assertEqual(last_number_fibonacci(5), 5)
        self.assertEqual(last_number_fibonacci(10), 5)
        self.assertEqual(last_number_fibonacci(20), 5)

if __name__ == '__main__':
    unittest.main()