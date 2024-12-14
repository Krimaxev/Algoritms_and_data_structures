import unittest
import time
import resource
from lab_6.task_2.src.main import phone_book_manager

class TestPhoneBookManager(unittest.TestCase):

    def test_phone_book_operations(self):
        lines = [
            "5",  # количество запросов
            "add 123 John",
            "add 456 Jane",
            "find 123",
            "find 789",
            "del 123"
        ]
        expected_output = ['John', 'not found']
        self.assertEqual(phone_book_manager(lines), expected_output)

    def test_performance(self):
        lines = ["100000"] + [f"add {i} Person{i}" for i in range(100000)]

        start_time = time.time()
        initial_mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

        phone_book_manager(lines)

        end_time = time.time()
        final_mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

        print(f"ЗАТРАТЫ ВРЕМЕНИ: {end_time - start_time} СЕКУНД")
        print(f"ЗАТРАТЫ ПАМЯТИ: {(final_mem - initial_mem) / 1024} Мб")


if __name__ == '__main__':
    unittest.main()