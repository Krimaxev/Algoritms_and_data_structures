import sys
import time
import resource
from lab_2.task_1.src.main_1 import *


if __name__ == "__main__":
    time_start = time.perf_counter()
    f, f2 = open("../txtf/test_1_input", "r"), open("../txtf/test_1_output", "w")
    l, l2 = int(f.readline()), f.readline()
    m = [int(x) for x in l2.split()]
    s = ''
    check = Check(l,m)

    m1 = Merge_sort(m)
    for j in range(len(m1)):
        s += str(m1[j])
        s += " "
    f2.write(s)

    time_elapsed = (time.perf_counter() - time_start)
    memMb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024.0
    print("ВРЕМЯ:", time_elapsed)
    print("Память:%5.1f МБ" % (memMb))
    print(f"Размер списка: {sys.getsizeof(m)} байт")

    f.close()
    f2.close()
