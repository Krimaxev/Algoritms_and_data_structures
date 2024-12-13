from lab_1.utils import operation_with_file, check, input_f, string, output_f


def insertion_sort(a):
    for i in range(1, len(a)):
        key = a[i]

        if isinstance(key, list):
            raise ValueError("Элемент массива является списком.")

        j = i - 1
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

if __name__=="__main__":
    FILE_INPUT = "../txtf/input_n1"
    FILE_OUTPUT = "../txtf/output_n1"
    file = operation_with_file(FILE_INPUT)
    len_list, values = file[0], file[1]
    check = check(len_list, values)
    if check:
        result = string(insertion_sort(values))
        output_f(FILE_OUTPUT, result)
        print("Входные данные корректны")
    else:
        output_f(FILE_OUTPUT, "ОШИБКА ВХОДНЫХ ДАННЫХ")
        raise ValueError("ОШИБКА ВХОДНЫХ ДАННЫХ")



