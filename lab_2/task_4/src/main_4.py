
def Binary_search(m, key):
    index = 0
    while index < len(m) and m[index] != key:
        index += 1
    if index < len(m):
        return index
    else:
        return -1

def Check(len_1,len_2,list_1,list_2):
    if (len_1==0 or len_1>10**5) or (len_2 == 0 or len_2 > 10 ** 5): return "Отсутствие/превышение лимита длины"
    if (len_1 != len(list_1)) or (len_2 != len(list_2)): return "Ошибка"
    for j in range(len(list_1)):
        if abs(list_1[j]) > 10 ** 9: return "Лимит одного из элементов превышен"
    for k in range(len(list_2)):
        if abs(list_2[k]) > 10 ** 9: return "Лимит одного из элементов превышен"

if __name__=="__main__":
    f1, f2 = open("../txtf/input_task_4", "r"), open("../txtf/output_task_4", "w")
    l1, l2, l3, l4 = int(f1.readline()), f1.readline(), int(f1.readline()), f1.readline()
    m1, m2 = [int(x) for x in l2.split()], [int(x) for x in l4.split()]
    check = Check(l1,l3,m1,m2)
    s = ''
    for i in range(len(m2)):
        t = str(Binary_search(m1, m2[i]))
        s+=t
        s+=' '
    f2.write(s)

    f1.close()
    f2.close()



