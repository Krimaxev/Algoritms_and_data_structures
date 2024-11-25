import sys
import time
import resource
from lab_3.task_1.src.main_1 import quicksort_threeway, quicksort_standard
from lab_3.utils import input_operation


if __name__=="__main__":

    input_f = "../txtf/input"
    output_f = "../txtf/output"
    input_f2 = "../txtf/hard_input"
    output_f2 = "../txtf/hard_output"

    time_start = time.perf_counter()

    result, result2 = input_operation(input_f), input_operation(input_f2)
    quicksort_threeway(result)
    quicksort_threeway(result2)

    time_elapsed = (time.perf_counter() - time_start)
    memMb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024.0
    print("ВРЕМЯ:", time_elapsed)
    print("Память:%5.1f МБ" % (memMb))
    print(f"Размер списка №1: {sys.getsizeof(result)} байт")
    print(f"Размер списка №2: {sys.getsizeof(result2) // 1024} Мбайт")

    time_start = time.perf_counter()

    result3, result4 = input_operation(input_f),input_operation(input_f2)
    quicksort_standard(result)
    quicksort_standard(result2)

    time_elapsed = (time.perf_counter() - time_start)
    memMb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024.0
    print()
    print("ВРЕМЯ:", time_elapsed)
    print("Память:%5.1f МБ" % (memMb))
    print(f"Размер списка №3: {sys.getsizeof(result)} байт")
    print(f"Размер списка №4: {sys.getsizeof(result2)//1024} Мбайт")


