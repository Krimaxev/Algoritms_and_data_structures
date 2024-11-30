from lab_3.utils import input_operation_z, input_operation_z_two, input_operation_z_three, output_operation, sixth_check

def sort_z(a, b):
    products = []
    for x in a:
        for y in b:
            products.append(x * y)

    products.sort()
    total_sum = sum(products[i] for i in range(0, len(products), 10))
    return total_sum

if __name__=="__main__":
    FILE_INPUT = "../txtf/input"
    FILE_OUTPUT = "../txtf/output"
    list = input_operation_z(FILE_INPUT)
    n, m = int(list[0]), int(list[1])
    a = input_operation_z_two(FILE_INPUT)
    b = input_operation_z_three(FILE_INPUT)
    if sixth_check(n,m,a,b):
        output_operation(FILE_OUTPUT, sort_z(a,b))
        print("Входные данные корректны")
    if not(sixth_check(n,m,a,b)):
        output_operation(FILE_OUTPUT, "Ошибка входных данных")
        print("Ошибка входных данных")




