import time
import resource
from lab_1.task_3.src.task3 import insertion_sort_three
from lab_1.utils import operation_with_file,check,string,write_s

if __name__=="__main__":
    time_start = time.perf_counter()

    FILE_INPUT = "../txtf/input_n3"
    FILE_OUTPUT = "../txtf/output_n3"
    file = operation_with_file(FILE_INPUT)
    len_list, values = file[0], file[1]
    check = check(len_list, values)
    if check:
        result = string(insertion_sort_three(values))
        write_s(FILE_OUTPUT, result)

        time_elapsed = (time.perf_counter() - time_start)
        memMb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024.0
        print("ВРЕМЯ:", time_elapsed)
        print("Память:%5.1f МБ" % (memMb))
    else:
        write_s(FILE_OUTPUT,"ОШИБКА ВХОДНЫХ ДАННЫХ")
        raise ValueError("ОШИБКА ВХОДНЫХ ДАННЫХ")