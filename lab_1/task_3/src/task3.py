
from lab_1.utils import operation_with_file, check,string,write_s

def insertion_sort_three(a):
    for j in range(len(a)):
        key = a[j]
        u = j-1
        while u>=0 and a[u]<key:
            a[u+1]=a[u]
            u = u-1
        a[u+1] = key
    return a

if __name__=="__main__":
    FILE_INPUT = "../txtf/input_n3"
    FILE_OUTPUT = "../txtf/output_n3"
    file = operation_with_file(FILE_INPUT)
    len_list, values = file[0], file[1]
    check = check(len_list, values)
    if check:
        result = string(insertion_sort_three(values))
        write_s(FILE_OUTPUT, result)
        print("Входные данные корректны")
    else:
        write_s(FILE_OUTPUT,"ОШИБКА ВХОДНЫХ ДАННЫХ")
        raise ValueError("ОШИБКА ВХОДНЫХ ДАННЫХ")

