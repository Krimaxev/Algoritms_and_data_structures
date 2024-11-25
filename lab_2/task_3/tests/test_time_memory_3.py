import sys
import time
import resource
from lab_2.task_3.src.main_3 import *
from lab_2.utils import *

if __name__=="__main__":
    time_start = time.perf_counter()

    file = operation_with_file("../txtf/input_task_3")
    res = inverse(file)
    check_list = check(input_file_n("../txtf/input_task_3"), operation_with_file("../txtf/input_task_3"))
    output = output_file("../txtf/output_task_3", str(res))

    time_elapsed = (time.perf_counter() - time_start)
    memMb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024.0
    print("ВРЕМЯ:", time_elapsed)
    print("Память:%5.1f МБ" % (memMb))
    print(f"Размер списка: {sys.getsizeof(file)} байт")