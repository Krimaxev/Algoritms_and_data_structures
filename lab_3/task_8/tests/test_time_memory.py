import time
import resource
from lab_3.task_8.src.main_8 import closest_points
from lab_3.utils import read_input,write_output, eighth_check, output_operation

if __name__ == "__main__":
    time_start = time.perf_counter()

    FILE_INPUT = "../txtf/input"
    FILE_OUTPUT = "../txtf/output"
    points, k = read_input(FILE_INPUT)
    point_check = eighth_check(FILE_INPUT)
    if point_check:
        result = closest_points(points, k)
        write_output(FILE_OUTPUT, result)

        time_elapsed = (time.perf_counter() - time_start)
        memMb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024.0
        print("ВРЕМЯ:", time_elapsed)
        print("Память:%5.1f МБ" % (memMb))
    else:
        output_operation(FILE_OUTPUT, "Ошибка входных данных")
        print("Ошибка входных данных")

