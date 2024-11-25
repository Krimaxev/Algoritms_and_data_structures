from lab_3.utils import input_operation_z, input_operation_z_two, input_operation_z_three, output_operation


def sort_z(file):
    list = input_operation_z(file)
    n,m = int(list[0]), int(list[1])
    a = input_operation_z_two(file)
    b = input_operation_z_three(file)

    products = []
    for x in a:
        for y in b:
            products.append(x * y)

    products.sort()
    total_sum = sum(products[i] for i in range(0, len(products), 10))
    return total_sum

if __name__=="__main__":
    output_operation("../txtf/output", sort_z("../txtf/input"))


