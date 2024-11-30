
def input_operation(a):
    f1 = open(a,"r")
    l = int(f1.readline())
    l2 = f1.readline()
    m = [int(x) for x in l2.split()]
    return m

def input_operation_z(a):
    f1 = open(a, "r")
    l2 = f1.readline()
    m = [int(x) for x in l2.split()]
    return m

def input_operation_z_two(a):
    f1 = open(a, "r")
    l = f1.readline()
    l2 = f1.readline()
    l3 = f1.readline()
    m = [int(x) for x in l2.split()]
    m2 = [int(x) for x in l3.split()]
    return m

def input_operation_z_three(a):
    f1 = open(a, "r")
    l = f1.readline()
    l2 = f1.readline()
    l3 = f1.readline()
    m = [int(x) for x in l2.split()]
    m2 = [int(x) for x in l3.split()]
    return m2

def input_operation_two(a):
    f1 = open(a,"r")
    l = f1.readline()
    l2 = f1.readline()
    m = [int(x) for x in l.split()]
    m2 = [int(x) for x in l2.split()]
    return m

def input_operation_three(a):
    f1 = open(a,"r")
    l = f1.readline()
    l2 = f1.readline()
    m = [int(x) for x in l.split()]
    m2 = [int(x) for x in l2.split()]
    return m2

def output_operation(a,b):
    f1 = open(a,"w")
    f1.write(str(b))

def open_f(a):
    f = open(a,"r")
    l = int(f.readline())
    return l

def string(a):
    s = ''
    for i in range(len(a)):
        s+=str(a[i])
        s+=' '
    return s[:-1]

def first_check(a):
    f = open(a,"r")
    len_1 = int(f.readline())
    list_1 = input_operation(a)
    if (len_1==0 or len_1>(2*10**5)):
        return False
    if (len_1 != len(list_1)):
        return False
    for j in range(len(list_1)):

        if abs(list_1[j]) > 10 ** 9:
            return False
    else:
        return True

def second_check(a):
    if a==0 or a>10**6:
        return False
    else:
        return True

def third_check(a):
    l1 = input_operation_two(a)
    l2 = input_operation_three(a)
    n,k = int(l1[0]), int(l1[1])
    if (n==0 or n > 10**5) or (k==0 or k>10**5):
        return False
    for i in range(len(l2)):
        if int(abs(l2[i])) > 10**9:
            return False
    else:
        return True

def sixth_check(n, m, a, b):
    if not (1<=n<=6000 and 1<=m<=6000):
        return False
    for i in range(len(a)):
        if not(0<=a[i]<=40000):
            return False
    for j in range(len(b)):
        if not(0<=b[j]<=40000):
            return False

    return True

def read_input(input_file):
    with open(input_file, 'r') as file:
        n, k = map(int, file.readline().strip().split())
        points = []
        for _ in range(n):
            x, y = map(int, file.readline().strip().split())
            points.append((x, y))
        return points, k

def read_input_nine(input_file):
    with open(input_file, 'r') as file:
        k = int(file.readline())
        points = []
        for _ in range(k):
            x, y = map(int, file.readline().strip().split())
            points.append((x, y))
        return points, k

def write_output(output_file, result):
    with open(output_file, 'w') as file:
        file.write(','.join([f"[{x},{y}]" for x, y in result]))

def eighth_check(input_file):
    with open(input_file, 'r') as file:
        n, k = map(int, file.readline().strip().split())
        points = []
        if not(1<=n<=10**5):
            return False
        for _ in range(n):
            x, y = map(int, file.readline().strip().split())
            points.append((x, y))
            if not(-10**9<=x<=10**9 or -10**9<=y<=10**9):
                return False
        else:
            return True

def nine_check(input_file):
    with open(input_file, 'r') as file:
        k = int(file.readline())
        points = []
        if not(1<=k<=10**5):
            return False
        for _ in range(k):
            x, y = map(int, file.readline().strip().split())
            points.append((x, y))
            if not(-10**9<=x<=10**9 or -10**9<=y<=10**9):
                return False
        else:
            return True

def read_input_n(file_name):
    with open(file_name, 'r') as file:
        n = int(file.readline().strip())
        points = [tuple(map(int, file.readline().split())) for _ in range(n)]
    return points







