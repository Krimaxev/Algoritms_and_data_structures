import os
import sys
import unittest
from io import StringIO


def discover_and_run_all_tests(base_dirs):
    print("\n========== Запуск всех тестов во всех лабораториях ==========\n")

    for base_path in base_dirs:
        print(f"\n--- Поиск и запуск тестов в директории: {base_path} ---")
        if not os.path.exists(base_path):
            print(f"Директория {base_path} не найдена. Пропускаем.")
            continue

        # Рекурсивно ищем папки 'test' в каждой 'task'
        for dirpath, dirnames, filenames in os.walk(base_path):
            if os.path.basename(dirpath) == "tests":

                # Добавляем текущую директорию с тестами в sys.path
                sys.path.insert(0, dirpath)

                try:
                    # Удаляем старые кэши импортов
                    for module in list(sys.modules.keys()):
                        if "test_" in module:
                            del sys.modules[module]

                    # Загружаем тесты
                    loader = unittest.TestLoader()
                    suite = loader.discover(start_dir=dirpath, pattern="test_*.py")

                    # Подавляем стандартный вывод TextTestRunner
                    buffer = StringIO()
                    runner = unittest.TextTestRunner(stream=buffer, verbosity=0)
                    result = runner.run(suite)

                    # Кастомный вывод
                    if result.wasSuccessful():
                        print(f"Все тесты в папке '{dirpath}' прошли успешно!")
                    else:
                        print(f"Есть есты в папке '{dirpath}', которые завершились с ошибками.")

                finally:
                    # Убираем путь из sys.path после завершения тестов
                    sys.path.pop(0)


if __name__ == "__main__":
    # Список директорий лабораторных работ
    base_dirs = ["lab_0","lab_1", "lab_2", "lab_3", "lab_4", "lab_5", "lab_6","lab_7"]

    # Добавляем текущую директорию в sys.path для корректного импорта
    sys.path.append(os.path.abspath("."))

    # Запускаем функцию
    discover_and_run_all_tests(base_dirs)