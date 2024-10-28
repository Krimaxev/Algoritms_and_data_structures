from lab_2.task_4.src.main_4 import *
import sys
import time
import resource

if __name__=="__main__":
    time_start = time.perf_counter()
    f1, f2 = open("../txtf/input_task_4", "r"), open("../txtf/output_task_4", "w")
    l1, l2, l3, l4 = int(f1.readline()), f1.readline(), int(f1.readline()), f1.readline()
    m1, m2 = [int(x) for x in l2.split()], [int(x) for x in l4.split()]
    check = Check(l1,l3,m1,m2)
    s = ''
    for i in range(len(m2)):
        t = str(Binary_search(m1, m2[i]))
        s+=t
        s+=' '
    f2.write(s)

    time_elapsed = (time.perf_counter() - time_start)
    memMb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024.0
    print("ВРЕМЯ:", time_elapsed)
    print("Память:%5.1f МБ" % (memMb))
    print(f"Размер списка №1: {sys.getsizeof(m1)} байт")
    print(f"Размер списка №2: {sys.getsizeof(m2)} байт")

    f1.close()
    f2.close()