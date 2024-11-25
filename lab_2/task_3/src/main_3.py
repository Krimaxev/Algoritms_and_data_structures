from lab_2.utils import *
def inverse(a):
    c = 0
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i]>a[j] and i<j:
                c+=1
    return c

if __name__=="__main__":
    file = operation_with_file("../txtf/input_task_3")
    res = inverse(file)
    check_list = check(input_file_n("../txtf/input_task_3"),operation_with_file("../txtf/input_task_3"))
    output = output_file("../txtf/output_task_3", str(res))


