from lab_2.utils import *
import sys
import time
import resource

if __name__=="__main__":
    time_start = time.perf_counter()

    file_1 = second_file_operation("../txtf/input_task_4")
    file_2 = second_file_operation_x("../txtf/input_task_4")
    check = second_check(second_file_operation_l1("../txtf/input_task_4"), second_file_operation_l3("../txtf/input_task_4"), file_1, file_2)
    result = string_task_four(file_1, file_2)
    file_o = output_file("../txtf/output_task_4", result)

    time_elapsed = (time.perf_counter() - time_start)
    memMb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024.0
    print("ВРЕМЯ:", time_elapsed)
    print("Память:%5.1f МБ" % (memMb))
    print(f"Размер списка №1: {sys.getsizeof(file_1)} байт")
    print(f"Размер списка №2: {sys.getsizeof(file_2)} байт")

