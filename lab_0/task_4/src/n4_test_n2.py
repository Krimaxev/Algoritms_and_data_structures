import time
import resource
from lab_0.utils import read_file_three,check_two,write_file

def fibonacci(input_number):
    fb1 = fb2 = 1
    for i in range(2, input_number):
        fb1, fb2 = fb2, fb1 + fb2
    number = str(fb2)
    return number

if __name__=="__main__":
    time_start = time.perf_counter()

    FILE_INPUT = "../txtf/n4_input_n2"
    FILE_OUTPUT = "../txtf/n4_output_n2"
    input_f = read_file_three(FILE_INPUT)
    check = check_two(input_f)

    if check:
        result = fibonacci(input_f)
        write_file(FILE_OUTPUT, result)

        time_elapsed = (time.perf_counter() - time_start)
        memMb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024.0

        print("ВРЕМЯ:", time_elapsed)
        print("Память:%5.1f МБ" % (memMb))
    else:
        write_file(FILE_OUTPUT, "ОШИБКА ВХОДНЫХ ДАННЫХ")
        raise ValueError("ОШИБКА ВХОДНЫХ ДАННЫХ")





