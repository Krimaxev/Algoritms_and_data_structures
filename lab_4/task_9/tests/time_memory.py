import sys
import time
import resource
from lab_4.task_9.src.main import process_requests
from lab_4.utils import read_input, check_nine, write_output, string_column

if __name__=="__main__":
    time_start = time.perf_counter()

    FILE_INPUT = "../txtf/input.txt"
    FILE_OUTPUT = "../txtf/output.txt"
    check = check_nine(FILE_INPUT)
    if check:
        list = read_input(FILE_INPUT)
        write_output(FILE_OUTPUT,string_column(process_requests(list[1:],list)))

        time_elapsed = (time.perf_counter() - time_start)
        memMb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024.0
        print("ВРЕМЯ:", time_elapsed)
        print("Память:%5.1f МБ" % (memMb))
        print(f"Размер списка: {sys.getsizeof(process_requests(list[1:],list))} байт")


    else:
        write_output(FILE_OUTPUT, "ОШИБКА ВХОДНЫХ ДАННЫХ")
        raise ValueError("ОШИБКА ВХОДНЫХ ДАННЫХ")