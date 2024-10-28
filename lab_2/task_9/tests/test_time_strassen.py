from lab_2.task_9.src.Strassen import *
import time
import resource


if __name__=="__main__":
    time_start = time.perf_counter()
    Check("../txtf/input_task_9", "../txtf/output_task_9")
    time_elapsed = (time.perf_counter() - time_start)
    memMb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024.0
    print("ВРЕМЯ:", time_elapsed)
    print("Память:%5.1f МБ" % (memMb))