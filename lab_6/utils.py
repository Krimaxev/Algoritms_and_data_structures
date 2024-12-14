# Функции для чтения файла, в зависимости от условия задачи
def read_file_one(file_path):
    f = open(file_path, "r")
    data = f.read().splitlines()
    return data[0], data[1:]

def read_file_four(file_path):
    with open(file_path, "r") as f:
        n = int(f.readline())
        operations = [line.strip().split() for line in f.readlines()][:n]

    return operations

def read_file_votes(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return lines

def read_file_stones(filename):

    with open(filename, 'r') as file:

        n, k = map(int, file.readline().split())

        S = file.readline().strip()

    return n, k, S

def read_value(file_path):
    f = open(file_path, "r")
    value = int(f.readline().strip())
    return value




# Функции для записи в файл, в зависимости от условия задачи
def write_one(file_path, result):
    with open(file_path, 'w') as outfile:
        outfile.write('\n'.join(result))

def write_file_back(file_path, result):
    f = open(file_path, "w")
    f.write(str(result))
    f.close()

def write_file_votes(file_path, votes):
    with open(file_path, 'w', encoding='utf-8') as file:
        for name in sorted(votes):
            file.write(f"{name} {votes[name]}\n")


# Функции для проверки входных данных файла, в зависимости от условия задачи
def check_first(n, m):
    if not(0<int(n)<=10**5):
        return False

    if int(n) != len(m):
        return False

    for i in range(len(m)):
        if not(abs(int(m[i][2]))<=10**18):
            return False

    return True

def check_second(n,m):
    if not(1<=int(n)<=10**5):
        return False
    if int(n) != len(m):
        return False
    return True

def check_four(n, m):
    if not(0<int(n)<=5*10**5):
        return False
    if int(n) != len(m):
        return False
    for i in range(len(m)):
        if not(len(m[i])<=20):
            return False
    return True

def check_stones(n, k):
    if not((1<=int(n)<=100000) and (1<=int(k)<=676)):
        return False
    return True

def check_value(n):
    if not(1<=int(n)<=10**4):
        return False
    return True

