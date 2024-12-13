from lab_5.utils import input_operation, output_operation, check_first_task

def heap(len_line, line):

    yes, no = "YES", "NO"
    for i in range(len_line):
        if 2 * (i + 1) - 1 < len_line:
            if line[i] > line[2 * (i + 1) - 1]:
                return no

        if 2 * (i + 1) < len_line:
            if line[i] > line[2 * (i + 1)]:
                return no

    return yes

if __name__=="__main__":
    FILE_INPUT = "../txtf/input.txt"
    FILE_OUTPUT = "../txtf/output.txt"
    input_f = input_operation(FILE_INPUT)
    length_line, line = input_f[0], input_f[1]
    check = check_first_task(length_line,line)
    result = heap(length_line,line)
    if check:
        output_operation(FILE_OUTPUT,result)
        print("Входные данные корректны")
    if not(check):
        output_operation(FILE_OUTPUT,"ОШИБКА ВХОДНЫХ ДАННЫХ")
        raise ValueError("ОШИБКА ВХОДНЫХ ДАННЫХ")





