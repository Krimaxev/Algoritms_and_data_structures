from lab_2.utils import *

def inverse(arr):
    count = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                count += 1
    return count

if __name__=="__main__":
    FILE_INPUT = "../txtf/input_task_3"
    FILE_OUTPUT = "../txtf/output_task_3"
    file = operation_with_file(FILE_INPUT)
    res = inverse(file)
    check_list = check(input_file_n(FILE_INPUT),operation_with_file(FILE_INPUT))
    if check_list:
        output = output_file(FILE_OUTPUT, str(res))
        print("Входные данные корректны")
    else:
        output_file(FILE_OUTPUT, "Ошибка входных данных")
        print("Ошибка входных данных")


