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
    FILE_INPUT = "../txtf/input_task_5"
    FILE_OUTPUT = "../txtf/output_task_5"
    file = operation_with_file(FILE_INPUT)
    check_f = check(input_file_n(FILE_INPUT),file)
    if check_f:
        res = majority(file)
        file_o = output_file(FILE_OUTPUT,str(res))
        print("В файле src задания №5 ЛР №2 код работает исправно")
    else:
        output_file(FILE_OUTPUT, "Ошибка входных данных")
        print("Ошибка входных данных")


