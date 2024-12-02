import sys
import time
import resource
from lab_3.task_6.scr.main_6 import sort_z
from lab_3.utils import output_operation, input_operation_z, input_operation_z_two, input_operation_z_three, sixth_check


if __name__=="__main__":
    time_start = time.perf_counter()

    FILE_INPUT = "../txtf/input"
    FILE_OUTPUT = "../txtf/output"
    list = input_operation_z(FILE_INPUT)
    n, m = int(list[0]), int(list[1])
    a = input_operation_z_two(FILE_INPUT)
    b = input_operation_z_three(FILE_INPUT)
    if sixth_check(n, m, a, b):
        output_operation(FILE_OUTPUT, sort_z(a, b))

        time_elapsed = (time.perf_counter() - time_start)
        memMb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024.0
        print("ВРЕМЯ:", time_elapsed)
        print("Память:%5.1f МБ" % (memMb))
        print(f"Размер списка: {sys.getsizeof(sort_z(a,b))} байт")
    if not (sixth_check(n, m, a, b)):
        output_operation(FILE_OUTPUT, "Ошибка входных данных")
        print("Ошибка входных данных")