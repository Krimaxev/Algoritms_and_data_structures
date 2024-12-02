from lab_4.utils import read_input, check_five, write_output, string_column

def process_stack(commands):
    stack = []
    max_stack = []
    results = []

    for command in commands:
        if command.startswith("push"):
            _, value = command.split()
            value = int(value)
            stack.append(value)

            if max_stack:
                max_stack.append(max(value, max_stack[-1]))
            else:
                max_stack.append(value)
        elif command.startswith("pop"):
            if stack:
                stack.pop()
                max_stack.pop()
        elif command.startswith("max"):

            if max_stack:
                results.append(str(max_stack[-1]))

    return results

if __name__=="__main__":
    FILE_INPUT = "../txtf/input.txt"
    FILE_OUTPUT = "../txtf/output.txt"
    list = read_input(FILE_INPUT)
    check = check_five(FILE_INPUT)
    if check:
        result = process_stack(list)
        write_output(FILE_OUTPUT,string_column(result))
        print("Входные данные корректны")
    else:
        write_output(FILE_OUTPUT, "ОШИБКА ВХОДНЫХ ДАННЫХ")
        raise ValueError("ОШИБКА ВХОДНЫХ ДАННЫХ")


