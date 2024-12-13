import time
import resource
from lab_5.task3.src.main import process_packets
from lab_5.utils import input_operation_task_three, check_third_task, output_operation

if __name__=="__main__":
    time_start = time.perf_counter()

    FILE_INPUT = "../txtf/input.txt"
    FILE_OUTPUT = "../txtf/output.txt"
    input_f = input_operation_task_three(FILE_INPUT)
    n, buf_size, packets = input_f[0], input_f[1], input_f[2]
    check = check_third_task(n, buf_size)
    if check:
        results = process_packets(buf_size, packets)
        output_operation(FILE_OUTPUT, results)

        time_elapsed = (time.perf_counter() - time_start)
        memMb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024.0
        print("ВРЕМЯ:", time_elapsed)
        print("Память:%5.1f МБ" % (memMb))
    else:
        output_operation(FILE_OUTPUT, "ОШИБКА ВХОДНЫХ ДАННЫХ")
        raise ValueError("ОШИБКА ВХОДНЫХ ДАНННЫХ")