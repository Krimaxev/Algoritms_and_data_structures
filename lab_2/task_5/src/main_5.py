from lab_2.utils import *

def majority(a):
    for i in range(len(a)):
        current_element = a[i]
        count = 0
        for j in range(len(a)):
            if a[j] == current_element:
                count += 1
        if count > (len(a)/2):
            return 1
    return 0

if __name__=="__main__":
    file = operation_with_file("../txtf/input_task_5")
    print(check(input_file_n("../txtf/input_task_5"),file))
    res = majority(file)
    file_o = output_file("../txtf/output_task_5",str(res))

