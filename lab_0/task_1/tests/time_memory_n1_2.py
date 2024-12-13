import time
import resource
from lab_0.utils import check_one
from lab_0.task_1.src.n1_2 import easy_operation

if __name__=="__main__":
    time_start = time.perf_counter()

    a, b = 10, 10
    check = check_one(a,b)
    if check:
        print(easy_operation(a,b))
        time_elapsed = (time.perf_counter() - time_start)
        memMb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024.0

        print("ВРЕМЯ:", time_elapsed)
        print("Память:%5.1f МБ" % (memMb))
    else:
        raise ValueError("ОШИБКА ВХОДНЫХ ДАННЫХ")