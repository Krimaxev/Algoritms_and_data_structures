import sys
import time
import resource
from lab_4.task_3.src.main import bracket_sequence
from lab_4.utils import read_input,write_output, check_three

if __name__=="__main__":
    time_start = time.perf_counter()

    FILE_INPUT = "../txtf/input.txt"
    FILE_OUTPUT = "../txtf/output.txt"
    list = read_input(FILE_INPUT)
    check = check_three(FILE_INPUT)
    if check:
        write_output(FILE_OUTPUT,bracket_sequence(list))

        time_elapsed = (time.perf_counter() - time_start)
        memMb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024.0
        print("ВРЕМЯ:", time_elapsed)
        print("Память:%5.1f МБ" % (memMb))
        print(f"Размер списка: {sys.getsizeof(bracket_sequence(list))} байт")
    else:
        write_output(FILE_OUTPUT, "ОШИБКА ВХОДНЫХ ДАННЫХ")
        raise ValueError("ОШИБКА ВХОДНЫХ ДАННЫХ")



