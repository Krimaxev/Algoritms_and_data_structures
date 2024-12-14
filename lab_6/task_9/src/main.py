from lab_6.utils import read_value, check_value, write_file_back


def hash_killer(value):
    result_strings = ''
    strings = []
    for i in range(value):
        unique_suffix = chr(97 + (i % 26)) * ((i // 26) + 1)
        strings.append("a" * 5 + unique_suffix)

    for j in range(len(strings)):
        result_strings += strings[j]
        result_strings += '\n'

    return result_strings


if __name__=="__main__":
    FILE_INPUT = "../txtf/input.txt"
    FILE_OUTPUT = "../txtf/output.txt"
    string_number = read_value(FILE_INPUT)
    check = check_value(string_number)
    if check:
        result = hash_killer(string_number)
        write_file_back(FILE_OUTPUT, result)
        print("Входные данные корректны")
    else:
        write_file_back(FILE_OUTPUT, "ОШИБКА ВХОДНЫХ ДАННЫХ")
        raise ValueError("ОШИБКА ВХОДНЫХ ДАННЫХ")


