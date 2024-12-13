from lab_0.utils import check_one

def summ(first_elem,second_elem):
    return first_elem + second_elem

if __name__=="__main__":
    a, b = map(int, input().split())
    check = check_one(a,b)
    if check:
        print(summ(a,b))
    else:
        raise ValueError("ОШИБКА ВХОДНЫХ ДАННЫХ")