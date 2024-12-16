from lab_2.utils import second_file_operation_list1,second_file_operation_list2,second_check,second_file_operation_line1,second_file_operation_line3, output_file, string

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def answer(a, b):
    return string([binary_search(a, index) for index in b])


if __name__=="__main__":
    FILE_INPUT = "../txtf/input_task_4"
    FILE_OUTPUT = "../txtf/output_task_4"
    file_1 = second_file_operation_list1(FILE_INPUT)
    file_2 = second_file_operation_list2(FILE_INPUT)
    line1 = second_file_operation_line1(FILE_INPUT)
    line3 = second_file_operation_line3(FILE_INPUT)
    check = second_check(line1,line3,file_1,file_2)
    if check:
        results = answer(file_1,file_2)
        file_o = output_file(FILE_OUTPUT, results)
        print("В файле src задания №4 ЛР №2 код работает исправно")
    else:
        file_o = output_file(FILE_OUTPUT, "Ошибка входных данных")
        print("Ошибка входных данных")










