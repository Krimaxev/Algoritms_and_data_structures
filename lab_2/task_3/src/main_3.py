
def Inverse(a):
    c = 0
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i]>a[j] and i<j:
                c+=1
    return c

def Check(len_1,list_1):
    if (len_1==0 or len_1>10**5):
        return "Отсутствие/превышение лимита длины"
    if (len_1 != len(list_1)):
        return "Ошибка"
    for j in range(len(list_1)):
        if abs(list_1[j]) > 10 ** 9:
            return "Лимит одного из элементов превышен"


if __name__=="__main__":
    f1,f2 = open("../txtf/input_task_3", "r"), open("../txtf/output_task_3", "w")
    l, l2 = int(f1.readline()), f1.readline()
    el = [int(x) for x in l2.split()]

    check = (l,el)
    res = Inverse(el)
    f2.write(str(res))

    f1.close()
    f2.close()


