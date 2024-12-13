import unittest
from lab_0.task_2.src.n2 import fibonacci

class TestFibonacci(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fibonacci(1), '1')
        self.assertEqual(fibonacci(2), '1')
        self.assertEqual(fibonacci(3), '2')
        self.assertEqual(fibonacci(4), '3')
        self.assertEqual(fibonacci(5), '5')
        self.assertEqual(fibonacci(6), '8')

if __name__ == '__main__':
    unittest.main()