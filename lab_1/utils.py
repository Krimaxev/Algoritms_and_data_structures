def operation_with_file(a):
    f1 = open(a, "r")
    n = int(f1.readline())
    l = f1.readline()
    m = [int(x) for x in l.split()]
    f1.close()
    return n, m

def operation_with_file_four(a):
    f1 = open(a, "r")
    m = [int(x) for x in f1.readline().split()]
    n = int(f1.readline())
    f1.close()
    return n, m

def input_f(a):
    f1 = open(a,"r")
    l = int(f1.readline())
    f1.close()
    return l

def output_f(a,res):
    f1 = open(a, "w")
    f1.write(str(res))
    f1.close()

def string(a):
    s = ''
    for z in range(len(a)):
        s += str(a[z])
        s += ' '
    return s[:-1]

def string_plus(a):
    s = ''
    for z in range(len(a)):
        s += str(a[z])
        s += ', '
    return s[:-2]

def convert_to_string(a):
    s = ''
    m1 = [str(x) for x in a]
    for i in m1:
        s += str(i)
        s += ' '
    return s

def convert_to_string_2(a):
    s = ''
    m1 = [str(x+1) for x in a]
    for i in m1:
        s += str(i)
        s += ' '
    return s

def write_s(a, res):
    f1 = open(a,"w")
    f1.writelines(str(res))
    f1.close()

def write_s_plus(a, res):
    f1 = open(a,"w")
    f1.writelines(str(res) +"\n")
    f1. close()

def check(l, m):
    if not(0<=l<=10**3):
        return False
    if l != len(m):
        return False
    for i in range(len(m)):
        if abs(m[i]) > 10 ** 9:
            return False
    return True

def check_four(n, m):

    if not(0<=len(m)<=10**3):
        return False

    if not(abs(n)<=10**3):
        return False

    return True

def check_task_two(a):
    f1 = open(a,"r")
    l1, l2 = int(f1.readline()), f1.readline()
    l2 = [int(x) for x in l2.split()]
    if l1!=len(l2):
        return "Длина строки не равна изначально указанной"
    else:
        return "Входные данные корректны"