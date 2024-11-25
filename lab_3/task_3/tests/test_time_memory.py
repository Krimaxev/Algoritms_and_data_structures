import sys
import time
import resource
from lab_3.task_3.src.main_3 import matreshka
from lab_3.utils import input_operation_two,input_operation_three,third_check,output_operation

if __name__=="__main__":
    l1 = input_operation_two("../txtf/input")
    l2 = input_operation_three("../txtf/input")
    n,k = int(l1[0]), int(l1[1])
    if third_check("../txtf/input") == "Входные данные корректны":
        time_start = time.perf_counter()
        res = matreshka(l2,k)
        if res == True:
            file_o = output_operation("../txtf/output","ДА")
        if res == False:
            file_o = output_operation("../txtf/output", "НЕТ")

        time_elapsed = (time.perf_counter() - time_start)
        memMb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024.0

        print(third_check("../txtf/input"))
        print("ВРЕМЯ:", time_elapsed)
        print("Память:%5.1f МБ" % (memMb))
        print(f"Размер списка: {sys.getsizeof(res)} байт")
    else:
        print(third_check("../txtf/input"))