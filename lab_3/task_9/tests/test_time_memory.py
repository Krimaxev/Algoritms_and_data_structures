import time
import resource
from lab_3.task_9.src.main_9 import closest_pair
from lab_3.utils import read_input_n,nine_check,output_operation


if __name__ == "__main__":
    time_start = time.perf_counter()

    FILE_INPUT = "../txtf/input"
    FILE_OUTPUT = "../txtf/output"
    points = read_input_n(FILE_INPUT)
    point_check = nine_check(FILE_INPUT)
    if point_check:
        result = closest_pair(points)
        output_operation(FILE_OUTPUT, result)

        time_elapsed = (time.perf_counter() - time_start)
        memMb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024.0
        print("ВРЕМЯ:", time_elapsed)
        print("Память:%5.1f МБ" % (memMb))
    else:
        output_operation(FILE_OUTPUT, "Ошибка входных данных")
        print("Ошибка входных данных")