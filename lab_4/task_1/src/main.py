from lab_4.utils import read_input, write_output, string, check


def steck(a):
    m = []
    for i in range(len(a)-1):
        if a[i+1]=="-" and len(a[i+1])==1:
            s = "".join(x for x in a[i] if x.isdecimal())
            m.append(s)
    return m

if __name__=="__main__":
    FILE_INPUT = "../txtf/input.txt"
    FILE_OUTPUT = "../txtf/output.txt"
    list = read_input(FILE_INPUT)
    check = check(FILE_INPUT)
    if check:
        result = string(steck(list))
        write_output(FILE_OUTPUT,result)
        print("Входные данные корректны")
    if not(check):
        write_output(FILE_OUTPUT, "ОШИБКА ВХОДНЫХ ДАННЫХ")
        raise ValueError("ОШИБКА ВХОДНЫХ ДАННЫХ")






