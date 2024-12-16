from lab_0.utils import check_one

def easy_operation(first_elem,second_elem):
    return first_elem + second_elem **2

if __name__=="__main__":
    a, b = 15, 15
    check = check_one(a,b)
    if check:
        print(easy_operation(a,b))
        print("В файле src задания №1 ЛР №0 код подзадания 1.2 работает исправно")
    else:
        raise ValueError("ОШИБКА ВХОДНЫХ ДАННЫХ")