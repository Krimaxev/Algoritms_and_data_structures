from lab_7.utils import read_split_lines, check_lines, write_split_lines, write_file


def levenshtein_distance_and_path(s1, s2):
    n, m = len(s1), len(s2)

    dp = [[0] * (m + 1) for _ in range(n + 1)]
    operations = [[None] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = i
        operations[i][0] = f"del {s1[i - 1]}" if i > 0 else None
    for j in range(m + 1):
        dp[0][j] = j
        operations[0][j] = f"add {s2[j - 1]}" if j > 0 else None

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
                operations[i][j] = "no_op"
            else:
                delete_cost = dp[i - 1][j] + 1
                insert_cost = dp[i][j - 1] + 1
                replace_cost = dp[i - 1][j - 1] + 1

                dp[i][j] = min(delete_cost, insert_cost, replace_cost)
                if dp[i][j] == delete_cost:
                    operations[i][j] = f"del {s1[i - 1]}"
                elif dp[i][j] == insert_cost:
                    operations[i][j] = f"add {s2[j - 1]}"
                elif dp[i][j] == replace_cost:
                    operations[i][j] = f"change {s1[i - 1]} {s2[j - 1]}"

    res_operations = []
    i, j = n, m
    while i > 0 or j > 0:
        current_op = operations[i][j]
        if current_op and current_op != "no_op":
            res_operations.append(current_op)

        if i > 0 and j > 0 and dp[i][j] == dp[i - 1][j - 1] + (1 if current_op and "change" in current_op else 0):
            i -= 1
            j -= 1
        elif i > 0 and dp[i][j] == dp[i - 1][j] + 1:
            i -= 1
        elif j > 0 and dp[i][j] == dp[i][j - 1] + 1:
            j -= 1

    res_operations.reverse()
    return dp[n][m], res_operations

if __name__=="__main__":
    FILE_INPUT = "../txtf/input.txt"
    FILE_OUTPUT = "../txtf/output.txt"
    file_i = read_split_lines(FILE_INPUT)
    l1, l2 = file_i[0], file_i[1]
    check = check_lines(l1, l2)
    if check:
        distance, result_operation = levenshtein_distance_and_path(l1, l2)
        write_split_lines(FILE_OUTPUT, distance, result_operation)
        print("В файле src задания №3 ЛР №7 код работает исправно")

    else:
        write_file(FILE_OUTPUT, "ОШИБКА ВХОДНЫХ ДАННЫХ")
        raise ValueError("ОШИБКА ВХОДНЫХ ДАННЫХ")




