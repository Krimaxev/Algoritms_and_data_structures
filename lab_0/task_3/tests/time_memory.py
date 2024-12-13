import time
import resource
from lab_0.task_3.src.n3 import last_number_fibonacci
from lab_0.utils import read_file_three,check_three,write_file


if __name__=="__main__":
    time_start = time.perf_counter()

    FILE_INPUT = "../txtf/fib2_input"
    FILE_OUTPUT = "../txtf/fib2_output"
    open_f = read_file_three(FILE_INPUT)
    check = check_three(open_f)
    if check:
        result = last_number_fibonacci(open_f)
        write_file(FILE_OUTPUT, result)

        time_elapsed = (time.perf_counter() - time_start)
        memMb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024.0

        print("ВРЕМЯ:", time_elapsed)
        print("Память:%5.1f МБ" % (memMb))
    else:
        write_file(FILE_OUTPUT, "ОШИБКА ВХОДНЫХ ДАННЫХ")
        raise ValueError("ОШИБКА ВХОДНЫХ ДАННЫХ")