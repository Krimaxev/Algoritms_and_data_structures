import sys
import time
import resource

from lab_1.n3.src.task3 import *

if __name__=="__main__":
    time_start = time.perf_counter()

    file = operation_with_file("../txtf/input_n3")
    ins_sort = string(file)
    w_1 = write_s("../txtf/output_n3", ins_sort)

    time_elapsed = (time.perf_counter() - time_start)
    memMb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024.0
    print("ВРЕМЯ:", time_elapsed)
    print("Память:%5.1f МБ" % (memMb))
    print(f"Размер списка: {sys.getsizeof(file)} байт")
