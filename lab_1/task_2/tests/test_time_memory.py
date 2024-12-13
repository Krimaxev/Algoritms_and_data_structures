from lab_1.task_2.src.task2 import *

import sys
import time
import resource

if __name__=="__main__":
    time_start = time.perf_counter()

    FILE_INPUT = "../txtf/input_n2"
    FILE_OUTPUT = "../txtf/output_n2"
    file = operation_with_file(FILE_INPUT)
    len_list, values = file[0], file[1]
    check = check(len_list, values)
    if check:
        ins_sort = insertion_sort_two(values)
        ins_sort_indices = insertion_sort_with_indices(len_list, values)
        conv_1 = str(convert_to_string(ins_sort_indices))
        conv_2 = str(convert_to_string_2(ins_sort))
        conv_3 = conv_2 + "\n" + conv_1
        write_s(FILE_OUTPUT, conv_3)

        time_elapsed = (time.perf_counter() - time_start)
        memMb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024.0
        print("ВРЕМЯ:", time_elapsed)
        print("Память:%5.1f МБ" % (memMb))
        print(f"Размер списка: {sys.getsizeof(file)} байт")
    else:
        write_s(FILE_OUTPUT, "ОШИБКА ВХОДНЫХ ДАННЫХ")
        raise ValueError("ОШИБКА ВХОДНЫХ ДАННЫХ")
