
def Merge(left_list, right_list):
    res = []
    i = j = 0

    left_len, right_len = len(left_list), len(right_list)

    for _ in range(left_len + right_len):
        if i < left_len and j < right_len:
            if left_list[i] <= right_list[j]:
                res.append(left_list[i])
                i += 1
            else:
                res.append(right_list[j])
                j += 1
        elif i == left_len:
            res.append(right_list[j])
            j += 1
        elif j == right_len:
            res.append(left_list[i])
            i += 1
    return res

def Merge_sort(x):
    if len(x) <= 1:
        return x

    median_x = len(x) // 2
    left_list = Merge_sort(x[:median_x])
    right_list = Merge_sort(x[median_x:])
    return Merge(left_list, right_list)

def Check(len_1,list_1):
    if (len_1==0 or len_1>(2*10**4)):
        return "Отсутствие/превышение лимита длины"
    if (len_1 != len(list_1)):
        return "Ошибка"
    for j in range(len(list_1)):
        if abs(list_1[j]) > 10 ** 9:
            return "Лимит одного из элементов превышен"

if __name__=="__main__":
    f, f2 = open("../txtf/input_task_1", "r"), open("../txtf/output_task_1", "w")
    l, l2 = int(f.readline()), f.readline()
    m = [int(x) for x in l2.split()]
    s = ''

    check = Check(l,m)

    m1 = Merge_sort(m)

    for j in range(len(m1)):
        s += str(m1[j])
        s += " "
    f2.write(s)

