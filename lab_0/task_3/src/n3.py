from lab_0.utils import read_file_three, check_three, write_file

def last_number_fibonacci(x):
    if x==0: return 0
    fb1,fb2 = 0,1
    for i in range(x-1):
        fb = (fb1+fb2)%10
        fb1,fb2 = fb2,fb
    return fb2

if __name__=="__main__":
    FILE_INPUT = "../txtf/fib2_input"
    FILE_OUTPUT = "../txtf/fib2_output"
    open_f = read_file_three(FILE_INPUT)
    check = check_three(open_f)
    if check:
        result = last_number_fibonacci(open_f)
        write_file(FILE_OUTPUT, result)
        print("Входные данные корректны")
    else:
        write_file(FILE_OUTPUT, "ОШИБКА ВХОДНЫХ ДАННЫХ")
        raise ValueError("ОШИБКА ВХОДНЫХ ДАННЫХ")







