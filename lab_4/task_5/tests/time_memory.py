import sys
import resource
import time
from lab_4.utils import read_input, check_five, write_output, string, string_column
from lab_4.task_5.src.main import process_stack

if __name__=="__main__":
    time_start = time.perf_counter()

    FILE_INPUT = "../txtf/input.txt"
    FILE_OUTPUT = "../txtf/output.txt"
    list = read_input(FILE_INPUT)
    check = check_five(FILE_INPUT)
    if check:
        result = process_stack(list)
        write_output(FILE_OUTPUT,string_column(result))

        time_elapsed = (time.perf_counter() - time_start)
        memMb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024.0
        print("ВРЕМЯ:", time_elapsed)
        print("Память:%5.1f МБ" % (memMb))
        print(f"Размер списка: {sys.getsizeof(process_stack(list))} байт")
    else:
        write_output(FILE_OUTPUT, "ОШИБКА ВХОДНЫХ ДАННЫХ")
        raise ValueError("ОШИБКА ВХОДНЫХ ДАННЫХ")