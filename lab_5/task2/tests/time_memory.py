import time
import resource
from lab_5.task2.src.main import compute_tree_height
from lab_5.utils import input_operation, check_second_task, output_operation


if __name__=="__main__":
    time_start = time.perf_counter()

    FILE_INPUT = "../txtf/input.txt"
    OUTPUT_FILE = "../txtf/output.txt"
    input_f = input_operation(FILE_INPUT)
    length_line, PARENTS = input_f[0], input_f[1]
    check = check_second_task(length_line,PARENTS)
    if check:
        result = compute_tree_height(length_line,PARENTS)
        output_operation(OUTPUT_FILE,result)

        time_elapsed = (time.perf_counter() - time_start)
        memMb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024.0
        print("ВРЕМЯ:", time_elapsed)
        print("Память:%5.1f МБ" % (memMb))
    else:
        output_operation(OUTPUT_FILE, "ОШИБКА ВХОДНЫХ ДАННЫХ")
        raise ValueError("ОШИБКА ВХОДНЫХ ДАННЫХ")