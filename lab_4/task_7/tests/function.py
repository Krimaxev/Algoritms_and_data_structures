import unittest
from lab_4.task_7.src.main import max_dynamic_sequence

class TestMaxDynamicSequence(unittest.TestCase):
    def test_case_1(self):
        n = 8
        a = [2, 7, 3, 1, 5, 2, 6, 2]
        m = 4
        self.assertEqual(max_dynamic_sequence(n, a, m), [7, 7, 5, 6, 6])

    def test_case_2(self):
        n = 5
        a = [1, 2, 3, 4, 5]
        m = 2
        self.assertEqual(max_dynamic_sequence(n, a, m), [2, 3, 4, 5])

    def test_case_3(self):
        n = 6
        a = [6, 5, 4, 3, 2, 1]
        m = 3
        self.assertEqual(max_dynamic_sequence(n, a, m), [6, 5, 4, 3])

    def test_case_4(self):
        n = 1
        a = [10]
        m = 1
        self.assertEqual(max_dynamic_sequence(n, a, m), [10])

    def test_case_5(self):
        n = 7
        a = [1, 3, 1, 2, 0, 5, 3]
        m = 4
        self.assertEqual(max_dynamic_sequence(n, a, m), [3, 3, 5, 5])

    def test_large_case(self):
        n = 100000
        a = list(range(1, 100001))
        m = 10

        expected_result = list(range(10, 100001))
        self.assertEqual(max_dynamic_sequence(n, a, m), expected_result)


if __name__ == "__main__":
    unittest.main()