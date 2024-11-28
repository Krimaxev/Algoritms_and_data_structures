
from lab_2.task_6.src.main_t_6 import *

def input_file_n(a):
    f = open(a,"r")
    n = int(f.readline())
    return n

def operation_with_file(a):
    f1 = open(a, "r")
    l1 = int(f1.readline())
    m = [int(x) for x in f1.readline().split()]
    f1.close()
    return m

def read_input(filepath):
    try:
        with open(filepath, 'r') as f:
            n = int(f.readline())
            line = f.readline().strip()
            return [int(x) for x in line.split()]
    except (FileNotFoundError, ValueError) as e:
        print(f"Ошибка при чтении входного файла: {e}")
        return None

def write_output(filepath, arr):
    try:
        with open(filepath, 'w') as f:
            f.write(' '.join(map(str, arr)))
    except Exception as e:
        print(f"Ошибка при записи в выходной файл: {e}")


def first_check(input_data, sorted_data):
    return sorted(input_data) == sorted_data

def second_file_operation_list1(a):
    f1 = open("../txtf/input_task_4", "r")
    l1, l2, l3, l4 = int(f1.readline()), f1.readline(), int(f1.readline()), f1.readline()
    m1, m2 = [int(x) for x in l2.split()], [int(x) for x in l4.split()]
    f1.close()
    return m1

def second_file_operation_list2(a):
    f1 = open("../txtf/input_task_4", "r")
    l1, l2, l3, l4 = int(f1.readline()), f1.readline(), int(f1.readline()), f1.readline()
    m1, m2 = [int(x) for x in l2.split()], [int(x) for x in l4.split()]
    f1.close()
    return m2

def second_file_operation_line1(a):
    f1 = open("../txtf/input_task_4", "r")
    l1, l2, l3, l4 = int(f1.readline()), f1.readline(), int(f1.readline()), f1.readline()
    f1.close()
    return l1

def second_file_operation_line3(a):
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

def first_check(len_1,list_1):
    if (len_1==0 or len_1>(2*10**5)):
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
        return False
    if (len_1 != len(list_1)):
        return False
    for j in range(len(list_1)):
        if abs(list_1[j]) > 10 ** 9:
            return False
    else:
        return True

def second_check(len_1,len_2,list_1,list_2):
    if (len_1==0 or len_1>10**5) or (len_2 == 0 or len_2 > 10 ** 5):
        return False
    if (len_1 != len(list_1)) or (len_2 != len(list_2)):
        return False
    for j in range(len(list_1)):
        if abs(list_1[j]) > 10 ** 9:
            return False
    for k in range(len(list_2)):
        if abs(list_2[k]) > 10 ** 9:
            return False
    else:
        return True


def subarray_operation(a, b):
    try:
        with open(a, "r") as f1, open(b, "w") as f2:
            lines = f1.readlines()
            price = []
            date = []

            for s in lines[1:]:
                parts = s.strip().split()
                if len(parts) == 2:
                    try:
                        date.append(parts[0])
                        price.append(float(parts[1]))
                    except ValueError as e:
                        print(f"Warning: Skipping invalid line: {s.strip()}  Error: {e}")
                        continue

            if not price:
                f2.write("No valid data available in the input file.\n")
                return

            result = max_subarray(price, date)

            if result[3] and result[4]:
                buy_price, sell_price, profit, buy_date, sell_date = result

                f2.write("Yandex\n"
                         "Change period: 1 month\n"
                         f"Date of purchase: {buy_date} Purchase price: {buy_price}\n"
                         f"Date of sale: {sell_date} Sale price: {sell_price}\n"
                         f"Profit: {profit}\n")
            else:
                f2.write("No profitable trading opportunity found.\n")

    except FileNotFoundError:
        print(f"Error: Input file '{a}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def price_subarray(a):
    f1 = open(a, "r")
    l = f1.readline()
    price, date = [], []
    for s in f1:
        c = 0
        a = [x for x in s.split()]
        c += 1
        price.append(float(a[1]))
        date.append(a[0])
    return price

def date_subarray(a):
    f1 = open(a, "r")
    l = f1.readline()
    price, date = [], []
    for s in f1:
        c = 0
        a = [x for x in s.split()]
        c += 1
        price.append(float(a[1]))
        date.append(a[0])
    return date