from lab_0.utils import read_file, write_file, check_one

def summ_file(a, b):
    return a + b

if __name__=="__main__":
    FILE_INPUT = "../txtf/input.txt"
    FILE_OUTPUT = "../txtf/output.txt"
    file = read_file(FILE_INPUT)
    first_elem, second_elem = file[0], file[1]
    check = check_one(first_elem, second_elem)
    if check:
        result = summ_file(first_elem, second_elem)
        write_file(FILE_OUTPUT, result)
        print("Входные данные корректны")
    else:
        write_file(FILE_OUTPUT, "ОШИБКА ВХОДНЫХ ДАННЫХ")
        raise ValueError("ОШИБКА ВХОДНЫХ ДАННЫХ")
