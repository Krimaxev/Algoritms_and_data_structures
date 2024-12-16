from lab_0.utils import read_file_three, check_two, write_file

def fibonacci(input_number):
    fb1 = fb2 = 1
    for i in range(2, input_number):
        fb1, fb2 = fb2, fb1 + fb2
    number = str(fb2)
    return number

if __name__=="__main__":
    FILE_INPUT = "../txtf/fib_input"
    FILE_OUTPUT = "../txtf/fib_output"
    input_f = read_file_three(FILE_INPUT)
    check = check_two(input_f)

    if check:
        result = fibonacci(input_f)
        write_file(FILE_OUTPUT, result)
        print("В файле src задания №2 ЛР №0 код работает исправно")
    else:
        write_file(FILE_OUTPUT, "ОШИБКА ВХОДНЫХ ДАННЫХ")
        raise ValueError("ОШИБКА ВХОДНЫХ ДАННЫХ")



