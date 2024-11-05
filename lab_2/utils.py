from lab_2.task_4.src.main_4 import *
from lab_2.task_6.src.main_t_6 import *
def input_file_n(a):
    f = open(a,"r")
    n = int(f.readline())
    return n

def operation_with_file(a):
    f1 = open(a, "r")
    n = int(f1.readline())
    m = [list(map(int, f1.readline().split())) for x in range(n)]
    f1.close()
    return m

def second_file_operation(a):
    f1 = open("../txtf/input_task_4", "r")
    l1, l2, l3, l4 = int(f1.readline()), f1.readline(), int(f1.readline()), f1.readline()
    m1, m2 = [int(x) for x in l2.split()], [int(x) for x in l4.split()]
    f1.close()
    return m1

def second_file_operation_x(a):
    f1 = open("../txtf/input_task_4", "r")
    l1, l2, l3, l4 = int(f1.readline()), f1.readline(), int(f1.readline()), f1.readline()
    m1, m2 = [int(x) for x in l2.split()], [int(x) for x in l4.split()]
    f1.close()
    return m2

def second_file_operation_l1(a):
    f1 = open("../txtf/input_task_4", "r")
    l1, l2, l3, l4 = int(f1.readline()), f1.readline(), int(f1.readline()), f1.readline()
    f1.close()
    return l1

def second_file_operation_l3(a):
    f1 = open("../txtf/input_task_4", "r")
    l1, l2, l3, l4 = int(f1.readline()), f1.readline(), int(f1.readline()), f1.readline()
    f1.close()
    return l3

def output_file(a,b):
    f2 = open(a,"w")
    f2.write(b)
    f2.close()

def string(a):
    s = ''
    for j in range(len(a)):
        s += str(a[j])
        s += " "
    return s

def string_task_four(a,b):
    s = ''
    for j in range(len(a)):
        s += str(binary_search(b,a[j]))
        s += " "
    return s

def first_check(len_1,list_1):
    if (len_1==0 or len_1>(2*10**4)):
        return "Отсутствие/превышение лимита длины"
    if (len_1 != len(list_1)):
        return "Ошибка"
    for j in range(len(list_1)):
        for k in list_1[j]:
            if abs(k) > 10 ** 9:
                return "Лимит одного из элементов превышен"
    else:
        return "Входные данные корректны"

def check(len_1,list_1):
    if (len_1==0 or len_1>10**5):
        return "Отсутствие/превышение лимита длины"
    if (len_1 != len(list_1)):
        return "Ошибка"
    for j in range(len(list_1)):
        for k in list_1[j]:
            if abs(k) > 10 ** 9:
                return "Лимит одного из элементов превышен"
    else:
        return "Входные данные корректны"

def second_check(len_1,len_2,list_1,list_2):
    if (len_1==0 or len_1>10**5) or (len_2 == 0 or len_2 > 10 ** 5): return "Отсутствие/превышение лимита длины"
    if (len_1 != len(list_1)) or (len_2 != len(list_2)): return "Ошибка"
    for j in range(len(list_1)):
        if abs(list_1[j]) > 10 ** 9: return "Лимит одного из элементов превышен"
    for k in range(len(list_2)):
        if abs(list_2[k]) > 10 ** 9: return "Лимит одного из элементов превышен"
    else:
        return "Входные данные корректны"

def subarray_operation(a,b):
    f1, f2 = open(a, "r"), open(b, "w")
    l = f1.readline()
    price, date = [], []
    for s in f1:
        c = 0
        a = [x for x in s.split()]
        c += 1
        price.append(float(a[1]))
        date.append(a[0])
    t = max_subarray(price)
    min_i, max_i = price.index(t[0]), price.index(t[1])
    buy_price, sell_price, profit = t[0], t[1], t[2]
    f2.write("Yandex\n"
             "Change period: 1 month\n"
             f"Date of purchase: {date[min_i]} Purchase price: {buy_price}\n"
             f"Date of sale: {date[max_i]} Sale price: {sell_price}\n"
             f"Profit: {profit}")
    f1.close()
    f2.close()