import unittest
from lab_3.task_2.src.main_2 import generate_worst_case

class TestGenerateWorstCase(unittest.TestCase):

    def test_empty_input(self):
        self.assertEqual(generate_worst_case(0), [])

    def test_single_element_input(self):
        self.assertEqual(generate_worst_case(1), [1])

    def test_small_input(self):
        result = generate_worst_case(5)
        self.assertEqual(len(result), 5)
        self.assertTrue(all(1 <= x <= 5 for x in result))  #Проверка диапазона значений

    def test_larger_input(self):
        result = generate_worst_case(100)
        self.assertEqual(len(result), 100)
        self.assertTrue(all(1 <= x <= 100 for x in result)) #Проверка диапазона значений

    def test_all_elements_present(self):
        result = generate_worst_case(10)
        self.assertEqual(sorted(result), list(range(1,11))) #Проверка наличия всех элементов


if __name__ == '__main__':
    unittest.main()