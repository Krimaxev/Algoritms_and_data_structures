import sys
import time
import resource
from lab_3.task_3.src.main_3 import matreshka
from lab_3.utils import input_operation_two,input_operation_three,third_check,output_operation

if __name__=="__main__":
    time_start = time.perf_counter()
    FILE_INPUT = "../txtf/input"
    FILE_OUTPUT = "../txtf/output"
    l1 = input_operation_two(FILE_INPUT)
    l2 = input_operation_three(FILE_INPUT)
    n, k = int(l1[0]), int(l1[1])
    THIRD_CHECK = third_check(FILE_INPUT)
    if THIRD_CHECK:
        result = matreshka(l2, k, n)
        if result:
            file_o = output_operation(FILE_OUTPUT, "ДА")
        if not (result):
            file_o = output_operation(FILE_OUTPUT, "НЕТ")

        time_elapsed = (time.perf_counter() - time_start)
        memMb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024.0

        print("ВРЕМЯ:", time_elapsed)
        print("Память:%5.1f МБ" % (memMb))
    else:
        output_operation(FILE_OUTPUT, "Входные данные некорректны")
        print("Входные данные некорректны")
