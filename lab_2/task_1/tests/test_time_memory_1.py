import sys
import time
import resource
from lab_2.task_1.src.main_1 import *
from lab_2.utils import *


if __name__ == "__main__":
    time_start = time.perf_counter()

    input_file = "../txtf/test_1_input"
    output_file = "../txtf/test_1_output"

    data = read_input(input_file)
    if data:
        sorted_data = merge_sort(data)
        write_output(output_file, sorted_data)

    print(first_check(input_file_n("../txtf/test_1_input"), operation_with_file("../txtf/test_1_input")))

    time_elapsed = (time.perf_counter() - time_start)
    memMb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024.0
    print("ВРЕМЯ:", time_elapsed)
    print("Память:%5.1f МБ" % (memMb))
    print(f"Размер списка: {sys.getsizeof(input_file)} байт")
