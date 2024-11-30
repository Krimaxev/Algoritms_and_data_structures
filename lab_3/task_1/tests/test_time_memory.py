import sys
import time
import resource
from lab_3.task_1.src.main_1 import quicksort_threeway, quicksort_standard
from lab_3.utils import input_operation, first_check, output_operation, string

if __name__=="__main__":
    time_start = time.perf_counter()

    input_f = "../txtf/input"
    output_f = "../txtf/output"
    input_f2 = "../txtf/hard_input"
    output_f2 = "../txtf/hard_output"
    FIRST_CHECK_1 = first_check("../txtf/input")
    FIRST_CHECK_2 = first_check("../txtf/hard_input")
    if FIRST_CHECK_1:
        result = input_operation(input_f)
        quicksort_threeway(result)
        output_operation(output_f, string(result))

        time_elapsed = (time.perf_counter() - time_start)
        memMb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024.0
        print("ВРЕМЯ №1:", time_elapsed)
        print("Память №1:%5.1f МБ" % (memMb))
        print(f"Размер списка №1: {sys.getsizeof(result)} байт")
    else:
        output_operation(output_f, "Ошибка входных данных")
        print(f"Ошибка входных данных в файле: {input_f}")

    print()

    if FIRST_CHECK_2:
        result2 = input_operation(input_f2)
        quicksort_threeway(result2)
        output_operation(output_f2, string(result2))
        time_elapsed = (time.perf_counter() - time_start)
        memMb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024.0
        print("ВРЕМЯ №2:", time_elapsed)
        print("Память №2:%5.1f МБ" % (memMb))
        print(f"Размер списка №2: {sys.getsizeof(result2) // 1024} Мбайт")
    else:
        output_operation(output_f2, "Ошибка входных данных")
        print(f"Ошибка входных данных в файле: {input_f2}")



