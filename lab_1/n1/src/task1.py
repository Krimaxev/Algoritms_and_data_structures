from lab_1.utils import *


def insertion_sort(a):
    for j in range(len(a)):
        key = a[j]
        u = j - 1
        while u >= 0 and a[u] > key:
            a[u + 1] = a[u]
            u = u - 1
        a[u + 1] = key
    return a

if __name__=="__main__":
    file = operation_with_file("../txtf/input_n1")
    print(check(input_f("../txtf/input_n1"), file))
    result = string(file)
    output = output_f("../txtf/output_n1", result)



