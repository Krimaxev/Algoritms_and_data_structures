import sys
import time
import resource
from lab_3.task_2.src.main_2 import generate_worst_case
from lab_3.utils import open_f,second_check,string,output_operation

if __name__ == "__main__":
    FILE_INPUT = "../txtf/input"
    FILE_OUTPUT = "../txtf/output"
    t = open_f(FILE_INPUT)
    if second_check(t):
        time_start = time.perf_counter()
        worst_case_permutation = generate_worst_case(t)
        res = string(worst_case_permutation)
        output_operation(FILE_OUTPUT,res)

        time_elapsed = (time.perf_counter() - time_start)
        memMb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024.0
        print("ВРЕМЯ:", time_elapsed)
        print("Память:%5.1f МБ" % (memMb))
        print(f"Размер списка: {sys.getsizeof(res)} байт")
    else:
        print("Входное значение некорректно")