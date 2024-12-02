import unittest
from lab_4.task_3.src.main import bracket_sequence

class TestBracketSequence(unittest.TestCase):
    def test_correct_sequences(self):
        # Тест на корректные последовательности
        self.assertEqual(bracket_sequence(["()", "[]", "([])", "()[]()"]), "ДА"+"\n" "ДА"+"\n" "ДА"+"\n" "ДА"+"\n")

    def test_incorrect_sequences(self):
        # Тест на некорректные последовательности
        self.assertEqual(bracket_sequence(["(", "[", "([)]", "())", "]["]), "НЕТ"+"\n" "НЕТ"+"\n" "НЕТ"+"\n" "НЕТ"+"\n" "НЕТ"+"\n")

    def test_mixed_sequences(self):
        # Тест на смешанные последовательности
        self.assertEqual(bracket_sequence(["([]", "[]()", "[)", "(([]))", "()"]),
                         "НЕТ"+"\n" "ДА"+"\n" "НЕТ"+"\n" "ДА"+"\n" "ДА"+"\n")

    def test_empty_string(self):
        # Тест на пустую строку
        self.assertEqual(bracket_sequence(["", "()"]), "ДА"+"\n" "ДА"+"\n")

    def test_nested_structures(self):
        # Тест на вложенные структуры
        self.assertEqual(bracket_sequence(["(((([[]]))))", "([[[[(((([]))))]]]])"]),
                         "ДА"+"\n" "ДА"+"\n")


if __name__ == "__main__":
    unittest.main()