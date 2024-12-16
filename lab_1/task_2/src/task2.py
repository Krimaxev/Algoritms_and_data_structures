from lab_1.utils import operation_with_file, convert_to_string, convert_to_string_2, write_s_plus, write_s, check


def insertion_sort_two(a):
    res = []
    for j in range(len(a)):
        key = a[j]
        u = j - 1
        while u >= 0 and a[u] > key:
            a[u + 1] = a[u]
            u = u - 1
        a[u + 1] = key
        res.append(a.index(key))
    return res

def insertion_sort_with_indices(n, arr):
    indices = list(range(n))
    for i in range(1, n):
        key = arr[i]
        key_index = indices[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            indices[j + 1] = indices[j]
            j -= 1
        arr[j + 1] = key
        indices[j + 1] = key_index


    result = [str(indices[i] + 1) for i in range(n)]
    return result

if __name__=="__main__":
    FILE_INPUT = "../txtf/input_n2"
    FILE_OUTPUT = "../txtf/output_n2"
    file = operation_with_file(FILE_INPUT)
    len_list, values = file[0], file[1]
    check = check(len_list,values)
    if check:
        ins_sort = insertion_sort_two(values)
        ins_sort_indices = insertion_sort_with_indices(len_list,values)
        conv_1 = str(convert_to_string(ins_sort_indices))
        conv_2 = str(convert_to_string_2(ins_sort))
        conv_3 = conv_2 + "\n" + conv_1
        write_s(FILE_OUTPUT,conv_3)
        print("В файле src задания №2 ЛР №1 код работает исправно")
    else:
        write_s(FILE_OUTPUT, "ОШИБКА ВХОДНЫХ ДАННЫХ")
        raise ValueError("ОШИБКА ВХОДНЫХ ДАННЫХ")

