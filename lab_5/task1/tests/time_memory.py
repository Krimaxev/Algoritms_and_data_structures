import resource
import time
from lab_5.task1.src.main import heap
from lab_5.utils import input_operation, check_first_task, output_operation

if __name__=="__main__":
    time_start = time.perf_counter()

    FILE_INPUT = "../txtf/input.txt"
    FILE_OUTPUT = "../txtf/output.txt"
    input_f = input_operation(FILE_INPUT)
    length_line, line = input_f[0], input_f[1]
    check = check_first_task(length_line,line)
    result = heap(length_line,line)
    if check:
        output_operation(FILE_OUTPUT,result)

        time_elapsed = (time.perf_counter() - time_start)
        memMb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024.0
        print("ВРЕМЯ:", time_elapsed)
        print("Память:%5.1f МБ" % (memMb))
    else:
        output_operation(FILE_OUTPUT,"ОШИБКА ВХОДНЫХ ДАННЫХ")
        raise ValueError("ОШИБКА ВХОДНЫХ ДАННЫХ")