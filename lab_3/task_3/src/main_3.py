from lab_3.utils import input_operation_two, input_operation_three, third_check, output_operation

def matreshka(arr, k, n):
    groups = [[] for _ in range(k)]
    for i in range(n):
        groups[i % k].append(arr[i])

    for group in groups:
        group.sort()

    sorted_arr = []
    for i in range(n):
        sorted_arr.append(groups[i % k][i // k])

    if sorted_arr == sorted(arr):
        return True
    else:
        return False

if __name__=="__main__":
    FILE_INPUT = "../txtf/input"
    FILE_OUTPUT = "../txtf/output"
    l1 = input_operation_two(FILE_INPUT)
    l2 = input_operation_three(FILE_INPUT)
    n,k = int(l1[0]), int(l1[1])
    THIRD_CHECK = third_check(FILE_INPUT)
    if THIRD_CHECK:
        result = matreshka(l2, k, n)
        if result:
            file_o = output_operation(FILE_OUTPUT,"ДА")
        if not(result):
            file_o = output_operation(FILE_OUTPUT, "НЕТ")
        print("Входные данные корректны")
    else:
        output_operation(FILE_OUTPUT, "Входные данные некорректны")
        print("Входные данные некорректны")












