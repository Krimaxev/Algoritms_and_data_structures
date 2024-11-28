import sys
import time
import resource
from lab_2.task_3.src.main_3 import *
from lab_2.utils import *

if __name__=="__main__":
    time_start = time.perf_counter()
    FILE_INPUT = "../txtf/input_task_3"
    FILE_OUTPUT = "../txtf/output_task_3"
    file = operation_with_file(FILE_INPUT)
    res = inverse(file)
    check_list = check(input_file_n(FILE_INPUT), operation_with_file(FILE_INPUT))
    if check_list:
        output = output_file(FILE_OUTPUT, str(res))
        print("Входные данные корректны")

        time_elapsed = (time.perf_counter() - time_start)
        memMb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024.0
        print("ВРЕМЯ:", time_elapsed)
        print("Память:%5.1f МБ" % (memMb))
        print(f"Размер списка: {sys.getsizeof(file)} байт")
    else:
        output_file(FILE_OUTPUT, "Ошибка входных данных")
        print("Ошибка входных данных")

