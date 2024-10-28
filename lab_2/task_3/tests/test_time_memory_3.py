import sys
import time
import resource
from lab_2.task_3.src.main_3 import *

if __name__=="__main__":
    time_start = time.perf_counter()
    f1,f2 = open("../txtf/input_task_3", "r"), open("../txtf/output_task_3", "w")
    l, l2 = int(f1.readline()), f1.readline()
    el = [int(x) for x in l2.split()]

    check = Check(l,el)
    res = Inverse(el)
    f2.write(str(res))

    time_elapsed = (time.perf_counter() - time_start)
    memMb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024.0
    print("ВРЕМЯ:", time_elapsed)
    print("Память:%5.1f МБ" % (memMb))
    print(f"Размер списка: {sys.getsizeof(el)} байт")

    f1.close()
    f2.close()