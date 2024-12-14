from lab_7.utils import read_lists, check_sequence, write_file


def longest_common_subsequence(a, b, c):
    n = len(a)
    m = len(b)
    l = len(c)

    dp = [[[0] * (l + 1) for _ in range(m + 1)] for __ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for k in range(1, l + 1):
                if a[i - 1] == b[j - 1] == c[k - 1]:
                    dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
                else:
                    dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])

    return dp[n][m][l]

if __name__=="__main__":
    FILE_INPUT = "../txtf/input.txt"
    FILE_OUTPUT = "../txtf/output.txt"
    file_i = read_lists(FILE_INPUT)
    sequence_1, sequence_2, sequence_3, len_1, len_2, len_3 = file_i[0], file_i[1], file_i[2], file_i[3], file_i[4], file_i[5]
    check = check_sequence(sequence_1, sequence_2, sequence_3, len_1, len_2, len_3)
    if check:
        result = longest_common_subsequence(sequence_1, sequence_2, sequence_3)
        write_file(FILE_OUTPUT, result)
        print("Входные данные корректны")
    else:
        write_file(FILE_OUTPUT, "ОШИБКА ВХОДНЫХ ДАННЫХ")
        raise ValueError("ОШИБКА ВХОДНЫХ ДАННЫХ")


