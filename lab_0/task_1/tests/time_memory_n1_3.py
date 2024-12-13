import time
import resource
from lab_0.task_1.src.n1_3 import summ_file
from lab_0.utils import read_file, check_one, write_file

if __name__=="__main__":
    time_start = time.perf_counter()

    FILE_INPUT = "../txtf/input.txt"
    FILE_OUTPUT = "../txtf/output.txt"
    file = read_file(FILE_INPUT)
    first_elem, second_elem = file[0], file[1]
    check = check_one(first_elem, second_elem)
    if check:
        result = summ_file(first_elem, second_elem)
        write_file(FILE_OUTPUT, result)

        time_elapsed = (time.perf_counter() - time_start)
        memMb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024.0

        print("ВРЕМЯ:", time_elapsed)
        print("Память:%5.1f МБ" % (memMb))
    else:
        write_file(FILE_OUTPUT, "ОШИБКА ВХОДНЫХ ДАННЫХ")
        raise ValueError("ОШИБКА ВХОДНЫХ ДАННЫХ")