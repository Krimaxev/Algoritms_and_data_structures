
def multiply(n, X, Y):
    Z = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                Z[i][j] += X[i][k]
                Z[i][j] += Y[k][j]
    return Z

def Check(file_i, file_o):
    with open(file_i, 'r') as f:
        n = int(f.readline())
        A = [list(map(int, f.readline().split())) for k in range(n)]
        B = [list(map(int, f.readline().split())) for k in range(n)]

        C = multiply(n, A, B)

    with open(file_o, 'w') as f:
        for res1 in C:
            f.write(' '.join(map(str, res1)) + '\n')


if __name__ == "__main__":
    Check("../txtf/input_task_9", "../txtf/output_task_9")
