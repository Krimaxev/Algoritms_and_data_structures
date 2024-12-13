import time
import resource
from lab_5.task5.src.main import job_scheduler
from lab_5.utils import input_operation_task_five, check_five_task, output_operation_five, output_operation

if __name__=="__main__":
    time_start = time.perf_counter()

    FILE_INPUT = "../txtf/input.txt"
    FILE_OUTPUT = "../txtf/output.txt"
    input_f = input_operation_task_five(FILE_INPUT)
    n, m, jobs = input_f[0], input_f[1], input_f[2]
    check = check_five_task(n, m, jobs)
    if check:
        result = job_scheduler(n, jobs)
        output_operation_five(FILE_OUTPUT,result)

        time_elapsed = (time.perf_counter() - time_start)
        memMb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024.0
        print("ВРЕМЯ:", time_elapsed)
        print("Память:%5.1f МБ" % (memMb))
    else:
        output_operation(FILE_OUTPUT,"ОШИБКА ВХОДНЫХ ДАННЫХ")
        raise ValueError("ОШИБКА ВХОДНЫХ ДАННЫХ")