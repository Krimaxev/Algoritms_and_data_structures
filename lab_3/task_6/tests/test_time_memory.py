import sys
import time
import resource
from lab_3.task_6.scr.main_6 import sort_z
from lab_3.utils import output_operation


if __name__=="__main__":
    time_start = time.perf_counter()

    output_operation("../txtf/output", sort_z("../txtf/input"))

    time_elapsed = (time.perf_counter() - time_start)
    memMb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024.0
    print("ВРЕМЯ:", time_elapsed)
    print("Память:%5.1f МБ" % (memMb))
    print(f"Размер списка: {sys.getsizeof(sort_z("../txtf/input"))} байт")