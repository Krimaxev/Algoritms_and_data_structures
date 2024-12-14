from lab_6.utils import read_file_stones, write_file_back, check_stones


def count_beautiful_pairs(string):
    beautiful_pairs = []
    for i in range(len(string)-1):
        if string[i] != string[i+1]:
            beautiful_pairs.append(string[i]+string[i+1])
    return len(beautiful_pairs)


if __name__=="__main__":
    FILE_INPUT = "../txtf/input.txt"
    FILE_OUTPUT = "../txtf/output.txt"
    read_f = read_file_stones(FILE_INPUT)
    n, k, S = read_f[0], read_f[1], read_f[2]
    check = check_stones(n, k)
    result = count_beautiful_pairs(S)
    if check:
        result = count_beautiful_pairs(S)
        write_file_back(FILE_OUTPUT, result)
        print("Входные данные корректны")
    else:
        write_file_back(FILE_OUTPUT, "ОШИБКА ВХОДНЫХ ДАННЫХ")
        raise ValueError("ОШИБКА ВХОДНЫХ ДАННЫХ")



