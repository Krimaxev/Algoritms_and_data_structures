import time
import resource
from lab_1.task_4.src.task4 import line_find
from lab_1.utils import operation_with_file_four, check_four, write_s

if __name__=="__main__":
    time_start = time.perf_counter()

    FILE_INPUT = "../txtf/input_n4"
    FILE_OUTPUT = "../txtf/output_n4"
    file_o = operation_with_file_four(FILE_INPUT)
    n, m = file_o[0], file_o[1]
    check = check_four(n, m)
    if check:
        result = line_find(n,m)
        write_s(FILE_OUTPUT,result)

        time_elapsed = (time.perf_counter() - time_start)
        memMb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024.0
        print("ВРЕМЯ:", time_elapsed)
        print("Память:%5.1f МБ" % (memMb))
    else:
        write_s(FILE_OUTPUT, "ОШИБКА ВХОДНЫХ ДАННЫХ")
        raise ValueError("ОШИБКА ВХОДНЫХ ДАННЫХ")