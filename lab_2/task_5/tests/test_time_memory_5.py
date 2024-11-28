from lab_2.task_5.src.main_5 import *
import sys
import time
import resource


if __name__=="__main__":
    time_start = time.perf_counter()

    file = operation_with_file("../txtf/input_task_5")
    check_f = check(input_file_n("../txtf/input_task_5"), file)
    if check_f:
        res = majority(file)
        file_o = output_file("../txtf/output_task_5", str(res))
        print("Входные данные корректны")

        time_elapsed = (time.perf_counter() - time_start)
        memMb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024.0
        print("ВРЕМЯ:", time_elapsed)
        print("Память:%5.1f МБ" % (memMb))
        print(f"Размер списка: {sys.getsizeof(file)} байт")
    else:
        output_file("../txtf/output_task_5", "Ошибка входных данных")
        print("Ошибка входных данных")



