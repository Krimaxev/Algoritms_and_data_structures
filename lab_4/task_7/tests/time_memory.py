import sys
import resource
import time
from lab_4.task_7.src.main import max_dynamic_sequence
from lab_4.utils import string, read_input_seven, check_seven, write_output

if __name__=="__main__":
    time_start = time.perf_counter()

    FILE_INPUT = "../txtf/input.txt"
    FILE_OUTPUT = "../txtf/output.txt"
    check = check_seven(FILE_INPUT)
    if check:
        argues = read_input_seven(FILE_INPUT)
        n, a, m = argues[0], argues[1], argues[2]
        result = max_dynamic_sequence(n, a, m)
        write_output(FILE_OUTPUT,string(result))

        time_elapsed = (time.perf_counter() - time_start)
        memMb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024.0
        print("ВРЕМЯ:", time_elapsed)
        print("Память:%5.1f МБ" % (memMb))
        print(f"Размер списка: {sys.getsizeof(result)} байт")

    else:
        write_output(FILE_OUTPUT, "ОШИБКА ВХОДНЫХ ДАННЫХ")
        raise ValueError("ОШИБКА ВХОДНЫХ ДАННЫХ")