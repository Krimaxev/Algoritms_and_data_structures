from lab_1.utils import operation_with_file, check, output_f, string

def selection_sort(a):
    for i in range(0,len(a)-1):
        mn = i
        for j in range(i+1,len(a)):
            if a[j]<a[mn]:
                mn = j
        a[i],a[mn] = a[mn],a[i]
    return a

if __name__=="__main__":
    FILE_INPUT = "../txtf/input_n5"
    FILE_OUTPUT = "../txtf/output_n5"
    input_f = operation_with_file(FILE_INPUT)
    len_list, list_f = input_f[0], input_f[1]
    check = check(len_list, list_f)
    if check:
        result = string(selection_sort(list_f))
        output_f(FILE_OUTPUT, result)
        print("Входные данные корректны")
    else:
        output_f(FILE_OUTPUT, "ОШИБКА ВХОДНЫХ ДАННЫХ")
        raise ValueError("ОШИБКА ВХОДНЫХ ДАННЫХ")