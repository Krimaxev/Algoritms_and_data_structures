from lab_3.utils import input_operation_two, input_operation_three, third_check, output_operation


def matreshka(m,k,i=0):
    l = len(m)
    if i == l - 1:
        return all(m[i] <= m[i+1] for i in range(l - 1))

    if all(m[i] <= m[i+1] for i in range(i, l - 1)):
        return True

    for j in range(i + 1, l):
        if (j - i) % k == 0 and m[j] < m[i]:
            new_m = m[:]
            new_m[j], new_m[i] = new_m[i], new_m[j]
            if matreshka(new_m,k,i+1):
                return True

    return False

if __name__=="__main__":
    l1 = input_operation_two("../txtf/input")
    l2 = input_operation_three("../txtf/input")
    n,k = int(l1[0]), int(l1[1])
    if third_check("../txtf/input") == "Входные данные корректны":
        res = matreshka(l2,k)
        if res == True:
            file_o = output_operation("../txtf/output","ДА")
        if res == False:
            file_o = output_operation("../txtf/output", "НЕТ")
        print(third_check("../txtf/input"))
    else:
        print(third_check("../txtf/input"))











