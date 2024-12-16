from lab_1.utils import operation_with_file_four, check_four, string, write_s, string_plus

def line_find(value, lists):
    not_result = "-1"
    values = [x for x,y in enumerate(lists) if y==value]
    if len(values)==0:
        return not_result
    if len(values) == 1:
        return string(values)
    else:
        return str(len(values)) + "\n" + string_plus(values)

if __name__=="__main__":
    FILE_INPUT = "../txtf/input_n4"
    FILE_OUTPUT = "../txtf/output_n4"
    file_o = operation_with_file_four(FILE_INPUT)
    n, m = file_o[0], file_o[1]
    check = check_four(n, m)
    if check:
        result = line_find(n,m)
        write_s(FILE_OUTPUT,result)
        print("В файле src задания №4 ЛР №1 код работает исправно")
    else:
        write_s(FILE_OUTPUT, "ОШИБКА ВХОДНЫХ ДАННЫХ")
        raise ValueError("ОШИБКА ВХОДНЫХ ДАННЫХ")