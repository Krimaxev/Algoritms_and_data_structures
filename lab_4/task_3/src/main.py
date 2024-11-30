from lab_4.utils import read_input, write_output, string, check_three, string_column


def bracket_sequence(a):
    results = []

    for s in a:
        stack = []
        is_valid = True

        for char in s:
            if char in "([":
                stack.append(char)
            elif char in ")]":
                if not stack:
                    is_valid = False
                    break
                top = stack.pop()

                if (top == '(' and char != ')') or (top == '[' and char != ']'):
                    is_valid = False
                    break

        if stack:
            is_valid = False

        results.append("ДА" if is_valid else "НЕТ")

    return string_column(results)


if __name__=="__main__":
    FILE_INPUT = "../txtf/input.txt"
    FILE_OUTPUT = "../txtf/output.txt"
    list = read_input(FILE_INPUT)
    check = check_three(FILE_INPUT)
    if check:
        write_output(FILE_OUTPUT,bracket_sequence(list))
        print("Входные данные корректны")
    else:
        raise ValueError("ОШИБКА ВХОДНЫХ ДАННЫХ")


