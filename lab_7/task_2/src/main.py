from lab_7.utils import read_integer, value_check, string_write, write_min_operation, write_file


def primitive_calculator(n):
    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + 1
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)

    sequence = []
    while n > 0:
        sequence.append(n)
        if n % 3 == 0 and dp[n] == dp[n // 3] + 1:
            n //= 3
        elif n % 2 == 0 and dp[n] == dp[n // 2] + 1:
            n //= 2
        else:
            n -= 1

    return len(sequence) - 1, list(reversed(sequence))

if __name__=="__main__":
    FILE_INPUT = "../txtf/input.txt"
    FILE_OUTPUT = "../txtf/output.txt"
    number = read_integer(FILE_INPUT)
    check = value_check(number)
    if check:
        min_operations, line_of_values = primitive_calculator(number)
        result = string_write(line_of_values)
        write_min_operation(FILE_OUTPUT, min_operations, result)
        print("В файле src задания №2 ЛР №7 код работает исправно")
    else:
        write_file(FILE_OUTPUT, "ОШИБКА ВХОДНЫХ ДАННЫХ")
        raise ValueError("ОШИБКА ВХОДНЫХ ДАННЫХ")


