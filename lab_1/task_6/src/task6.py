from lab_1.utils import operation_with_file, check, output_f, string


def bubble_sort(a):
    for i in range(len(a) - 1):
        for j in range(len(a) - 1, i, -1):
            if a[j] < a[j - 1]:
                a[j], a[j - 1] = a[j - 1], a[j]
    return a

if __name__=="__main__":
    FILE_INPUT = "../txtf/hi_input_n6"
    FILE_OUTPUT = "../txtf/output_n6"
    input_f = operation_with_file(FILE_INPUT)
    len_list, values = input_f[0], input_f[1]
    check = check(len_list,values)
    if check:
        result = string(bubble_sort(values))
        output_f(FILE_OUTPUT,result)
        print("Входные данные корректны")
    else:
        output_f(FILE_OUTPUT, "ОШИБКА ВХОДНЫХ ДАННЫХ")
        raise ValueError("ОШИБКА ВХОДНЫХ ДАННЫХ")

