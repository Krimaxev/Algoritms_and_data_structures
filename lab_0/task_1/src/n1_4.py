from lab_0.utils import read_file, check_one, write_file

def easy_operation_file(a, b):
    return a + b ** 2

if __name__=="__main__":
    FILE_INPUT = "../txtf/input.txt"
    FILE_OUTPUT = "../txtf/output.txt"
    file = read_file(FILE_INPUT)
    first_elem, second_elem = file[0], file[1]
    check = check_one(first_elem, second_elem)
    if check:
        result = easy_operation_file(first_elem, second_elem)
        write_file(FILE_OUTPUT, result)
        print("В файле src задания №1 ЛР №0 код подзадания 1.4 работает исправно")
    else:
        write_file(FILE_OUTPUT, "ОШИБКА ВХОДНЫХ ДАННЫХ")
        raise ValueError("ОШИБКА ВХОДНЫХ ДАННЫХ")