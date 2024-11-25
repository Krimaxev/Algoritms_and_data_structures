from lab_2.utils import *
import sys
import time
import resource

if __name__=="__main__":
    time_start = time.perf_counter()

    subarray_operation("../txtf/input_task_6", "../txtf/output_task_6")

    time_elapsed = (time.perf_counter() - time_start)
    memMb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024.0
    print("ВРЕМЯ:", time_elapsed)
    print("Память:%5.1f МБ" % (memMb))
    print(f"Размер списка цен: {sys.getsizeof(price_subarray("../txtf/input_task_6"))} байт")
    print(f"Размер списка дат: {sys.getsizeof(date_subarray("../txtf/input_task_6"))} байт")