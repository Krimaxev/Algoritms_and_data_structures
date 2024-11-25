from lab_1.n2.src.task2 import *

import sys
import time
import resource

if __name__=="__main__":
    time_start = time.perf_counter()

    file = operation_with_file("../txtf/input_n2")
    ins_sort = insertion_sort(file)
    conv_1 = convert_to_string(file)
    conv_2 = convert_to_string(ins_sort)
    w_1 = write_s_plus("../txtf/output_n2",conv_2)
    w_2 = write_s("../txtf/output_n2", conv_1)

    time_elapsed = (time.perf_counter() - time_start)
    memMb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024.0
    print("ВРЕМЯ:", time_elapsed)
    print("Память:%5.1f МБ" % (memMb))
    print(f"Размер списка: {sys.getsizeof(file)} байт")