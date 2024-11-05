from lab_2.utils import *

def binary_search(m, key):
    index = 0
    while index < len(m) and m[index] != key:
        index += 1
    if index < len(m):
        return index
    else:
        return -1

if __name__=="__main__":
    file_1 = second_file_operation("../txtf/input_task_4")
    file_2 = second_file_operation_x("../txtf/input_task_4")
    check = second_check(second_file_operation_l1("../txtf/input_task_4"),second_file_operation_l3("../txtf/input_task_4"),file_1,file_2)
    result = string_task_four(file_1,file_2)
    file_o = output_file("../txtf/output_task_4", result)



