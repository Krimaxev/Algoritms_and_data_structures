
def Majority(a):
    for i in range(len(a)):
        current_element = a[i]
        count = 0
        for j in range(len(a)):
            if a[j] == current_element:
                count += 1
        if count > (len(a)/2):
            return 1
    return 0

def Check(len_1,list_1):
    if len_1==0 or len_1>10**5:
        return "Отсутствие/превышение лимита длины"
    if len_1 != len(list_1):
        return "Ошибка"
    for j in range(len(list_1)):
        if abs(list_1[j]) > 10 ** 9:
            return "Лимит одного из элементов превышен"


if __name__=="__main__":
    f1,f2 = open("../txtf/input_task_5", "r"), open("../txtf/output_task_5", "w")
    l, l2 = int(f1.readline()), f1.readline()
    m = [int(x) for x in l2.split()]
    check = (l,m)

    res = Majority(m)
    f2.write(str(res))

    f1.close()
    f2.close()
