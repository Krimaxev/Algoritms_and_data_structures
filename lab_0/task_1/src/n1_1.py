from lab_0.utils import check_one

def summ(first_elem,second_elem):
    return first_elem + second_elem

if __name__=="__main__":
    a, b = 10, 10
    check = check_one(a,b)
    if check:
        print(summ(a,b))
        print("В файле src задания №1 ЛР №0 код подзадания 1.1 работает исправно")
    else:
        raise ValueError("ОШИБКА ВХОДНЫХ ДАННЫХ")