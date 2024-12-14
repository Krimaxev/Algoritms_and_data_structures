import time
import resource
from lab_6.task_1.src.main import process_operations
from lab_6.utils import read_file_one, check_first, write_one


if __name__=="__main__":
    time_start = time.perf_counter()

    FILE_INPUT = "../txtf/input.txt"
    FILE_OUTPUT = "../txtf/output.txt"
    file_i = read_file_one(FILE_INPUT)
    num_operations, operations = file_i[0], file_i[1]
    check = check_first(num_operations, operations)
    if check:
        result = process_operations(operations)
        write_one(FILE_OUTPUT, result)

        time_elapsed = (time.perf_counter() - time_start)
        memMb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024.0
        print("ВРЕМЯ:", time_elapsed)
        print("Память:%5.1f МБ" % (memMb))
    else:
        write_one(FILE_OUTPUT, "ОШИБКА ВХОДНЫХ ДАННЫХ")
        raise ValueError("ОШИБКА ВХОДНЫХ ДАННЫХ")
