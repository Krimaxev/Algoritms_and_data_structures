from lab_2.utils import *
from lab_2.task_4.src.main_4 import answer
import sys
import time
import resource

if __name__=="__main__":
    time_start = time.perf_counter()

    FILE_INPUT = "../txtf/input_task_4"
    FILE_OUTPUT = "../txtf/output_task_4"
    file_1 = second_file_operation_list1(FILE_INPUT)
    file_2 = second_file_operation_list2(FILE_INPUT)
    line1 = second_file_operation_line1(FILE_INPUT)
    line3 = second_file_operation_line3(FILE_INPUT)
    check = second_check(line1, line3, file_1, file_2)
    if check:
        time_start = time.perf_counter()
        results = answer(file_1, file_2)
        file_o = output_file(FILE_OUTPUT, results)
        print("Входные данные корректны")

        time_elapsed = (time.perf_counter() - time_start)
        memMb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024.0
        print("ВРЕМЯ:", time_elapsed)
        print("Память:%5.1f МБ" % (memMb))
        print(f"Размер списка №1: {sys.getsizeof(file_1)} байт")
        print(f"Размер списка №2: {sys.getsizeof(file_2)} байт")
    else:
        file_o = output_file(FILE_OUTPUT, "Ошибка входных данных")
        print("Ошибка входных данных")



