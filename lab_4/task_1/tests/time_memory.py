import sys
import time
import resource
from lab_4.task_1.src.main import steck
from lab_4.utils import read_input, write_output, check, string_column

if __name__=="__main__":
    time_start = time.perf_counter()

    FILE_INPUT = "../txtf/input.txt"
    FILE_OUTPUT = "../txtf/output.txt"
    list = read_input(FILE_INPUT)
    check = check(FILE_INPUT)
    if check:
        result = string_column(steck(list))
        write_output(FILE_OUTPUT,result)

        time_elapsed = (time.perf_counter() - time_start)
        memMb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024.0
        print("ВРЕМЯ:", time_elapsed)
        print("Память:%5.1f МБ" % (memMb))
        print(f"Размер списка: {sys.getsizeof(steck(list))} байт")
    if not(check):
        write_output(FILE_OUTPUT, "ОШИБКА ВХОДНЫХ ДАННЫХ")
        raise ValueError("ОШИБКА ВХОДНЫХ ДАННЫХ")
