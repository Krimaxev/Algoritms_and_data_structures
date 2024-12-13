import time
import resource
from lab_1.task_6.src.task6 import bubble_sort
from lab_1.utils import operation_with_file, check, string, output_f


if __name__=="__main__":
    time_start = time.perf_counter()

    FILE_INPUT = "../txtf/hi_input_n6"
    FILE_OUTPUT = "../txtf/output_n6"
    input_f = operation_with_file(FILE_INPUT)
    len_list, values = input_f[0], input_f[1]
    check = check(len_list,values)
    if check:
        result = string(bubble_sort(values))
        output_f(FILE_OUTPUT,result)

        time_elapsed = (time.perf_counter() - time_start)
        memMb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024.0
        print("ВРЕМЯ:", time_elapsed)
        print("Память:%5.1f МБ" % (memMb))
    else:
        output_f(FILE_OUTPUT, "ОШИБКА ВХОДНЫХ ДАННЫХ")
        raise ValueError("ОШИБКА ВХОДНЫХ ДАННЫХ")