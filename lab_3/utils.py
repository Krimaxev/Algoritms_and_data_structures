
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
        return "Отсутствие/превышение лимита длины"
    if (len_1 != len(list_1)):
        return "Ошибка"
    for j in range(len(list_1)):

        if abs(list_1[j]) > 10 ** 9:
            return "Лимит одного из элементов превышен"
    else:
        return "Входные данные корректны"

def second_check(a):
    if a==0 or a>10**6:
        return "Введенное значение некорректно"
    else:
        return "Входное значение корректно"

def third_check(a):
    l1 = input_operation_two(a)
    l2 = input_operation_three(a)
    n,k = int(l1[0]), int(l1[1])
    if (n==0 or n > 10**5) or (k==0 or k>10**5):
        return "Входные данные для n и k некорректны"
    for i in range(len(l2)):
        if int(abs(l2[i])) > 10**9:
            return "Лимит модуля одного из чесел превышен"
    else:
        return "Входные данные корректны"




