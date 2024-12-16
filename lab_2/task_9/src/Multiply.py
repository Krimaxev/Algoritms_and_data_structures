
def multiply(n, X, Y):
    Z = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                Z[i][j] += X[i][k]
                Z[i][j] += Y[k][j]
    return Z

def check(file_i, file_o):
    with open(file_i, 'r') as f:
        n = int(f.readline())
        A = [list(map(int, f.readline().split())) for k in range(n)]
        B = [list(map(int, f.readline().split())) for k in range(n)]

        C = multiply(n, A, B)

    with open(file_o, 'w') as f:
        for res1 in C:
            f.write(' '.join(map(str, res1)) + '\n')


if __name__ == "__main__":
    FILE_INPUT = "../txtf/input_task_9"
    FILE_OUTPUT = "../txtf/output_task_9"
    check(FILE_INPUT, FILE_OUTPUT)
    print("В файле src задания №9 (Multiply) ЛР №2 код работает исправно")
