import time
import resource
from lab_0.utils import read_file_three, check_three, write_file

def last_fibonacci(x):
    if x==0: return 0
    fb1,fb2 = 0,1
    for i in range(x-1):
        fb = (fb1+fb2)%10
        fb1,fb2 = fb2,fb
    return fb2

if __name__=="__main__":
    time_start = time.perf_counter()

    FILE_INPUT = "../txtf/n4_input_n3"
    FILE_OUTPUT = "../txtf/n4_output_n3"
    open_f = read_file_three(FILE_INPUT)
    check = check_three(open_f)
    if check:
        result = last_fibonacci(open_f)

        time_elapsed = (time.perf_counter() - time_start)
        memMb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024.0

        print("ВРЕМЯ:", time_elapsed)
        print("Память:%5.1f МБ" % (memMb))
    else:
        write_file(FILE_OUTPUT, "ОШИБКА ВХОДНЫХ ДАННЫХ")
        raise ValueError("ОШИБКА ВХОДНЫХ ДАННЫХ")







