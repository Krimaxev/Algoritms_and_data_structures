def read_file_coins(file_path):
    with open(file_path, "r") as fin:
        first_line = fin.readline().strip().split()
        money = int(first_line[0])
        k = int(first_line[1])

        second_line = fin.readline().strip().split()
        coins = list(map(int, second_line[:k]))


        return money, coins, k

def read_integer(file_path):
    f = open(file_path, "r")
    value = int(f.readline())
    return value

def read_split_lines(file_path):
    with open(file_path, "r") as f:
        s1 = f.readline()
        s2 = f.readline()
    return s1, s2

def read_lists(file_path):
    with open(file_path, "r") as inp:
        n = int(inp.readline())
        a = list(map(int, inp.readline().split()))
        m = int(inp.readline())
        b = list(map(int, inp.readline().split()))
        l = int(inp.readline())
        c = list(map(int, inp.readline().split()))
    return a,b,c,n,m,l


def string_write(m):
    s = ''
    for i in range(len(m)):
        s += str(m[i])
        s += ' '
    return s[:-1]


def write_file(file_path, result):
    f = open(file_path, "w")
    f.write(str(result))
    f.close()

def write_min_operation(file_path, min_o, results):
    f = open(file_path,"w")
    f.write(str(min_o)+"\n")
    f.write(str(results))

def write_split_lines(file_path, value_1, value_2):
    with open(file_path, "w") as f:
        f.write(str(value_1) + "\n")
        for op in value_2:
            f.write(op + "\n")



def check_money(money, k, coin):

    if not(1<=int(money)<=10**3):
        return False
    if not(1<=int(k)<=100):
        return False
    if int(k) != len(coin):
        return False

    for i in range(len(coin)):
        if not(1<=int(coin[i])<=10**3):
            return False

    return True

def value_check(n):
    if not(1<=int(n)<=10**6):
        return False
    return True

def check_lines(line_1, line_2):
    if not((1<=len(line_1)<=5000) and (1<=len(line_2)<=5000)):
        return False
    return True

def check_sequence(s1,s2,s3,l1,l2,l3):
    if not((1<=int(l1)<=100) and (1<=int(l2)<=100) and (1<=int(l3)<=100)):
        return False

    if (int(l1) != len(s1)) or (int(l2) != len(s2)) or (int(l3) != len(s3)):
        return False

    for i in range(len(s1)):
        if not(abs(int(s1[i]))<=10**9):
            return False

    for j in range(len(s2)):
        if not(abs(int(s1[j]))<=10**9):
            return False

    for k in range(len(s3)):
        if not(abs(int(s1[k]))<=10**9):
            return False

    return True






