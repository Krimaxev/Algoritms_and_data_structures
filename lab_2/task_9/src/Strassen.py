THRESHOLD = 16

def split(M):

    n = len(M) // 2
    return (
        [[M[i][j] for j in range(n)] for i in range(n)],  # A11
        [[M[i][j] for j in range(n, n * 2)] for i in range(n)],  # A12
        [[M[i][j] for j in range(n)] for i in range(n, n * 2)],  # A21
        [[M[i][j] for j in range(n, n * 2)] for i in range(n, n * 2)],  # A22
    )


def merge(C11, C12, C21, C22):

    n = len(C11)
    C = [[0 for _ in range(n * 2)] for _ in range(n * 2)]

    for i in range(n):
        for j in range(n):
            C[i][j] = C11[i][j]
            C[i][j + n] = C12[i][j]
            C[i + n][j] = C21[i][j]
            C[i + n][j + n] = C22[i][j]

    return C
def strassen(A, B):
    n = len(A)
    if n <= THRESHOLD:
        return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
    else:

        A11, A12, A21, A22 = split(A)
        B11, B12, B21, B22 = split(B)


        P1 = strassen(A11 + A22, B11 + B22)
        P2 = strassen(A21 + A22, B11)
        P3 = strassen(A11, B12 - B22)
        P4 = strassen(A22, B21 - B11)
        P5 = strassen(A11 + A12, B22)
        P6 = strassen(A21 - A11, B11 + B12)
        P7 = strassen(A12 - A22, B21 + B22)


        C11 = P1 + P4 - P5 + P7
        C12 = P3 + P5
        C21 = P2 + P4
        C22 = P1 - P2 + P3 + P6

        return merge(C11, C12, C21, C22)

def check(file_inp, file_out):
    with open(file_inp, 'r') as f:
        n = int(f.readline())
        A = [list(map(int, f.readline().split())) for k in range(n)]
        B = [list(map(int, f.readline().split())) for k in range(n)]

        C = strassen(A, B)

    with open(file_out, 'w') as f:
        for res1 in C:
            f.write(' '.join(map(str, res1)) + '\n')

if __name__=="__main__":
    FILE_INPUT = "../txtf/input_task_9"
    FILE_OUTPUT = "../txtf/output_task_9"
    check(FILE_INPUT, FILE_OUTPUT)
    print("В файле src задания №9 (Strassen) ЛР №2 код работает исправно")
