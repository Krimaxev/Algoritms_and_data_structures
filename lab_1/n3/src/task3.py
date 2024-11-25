from lab_1.utils import *

def insertion_sort_3(a):
    for j in range(len(a)):
        key = a[j]
        u = j-1
        while u>=0 and a[u]<key:
            a[u+1]=a[u]
            u = u-1
        a[u+1] = key
    return a

if __name__=="__main__":
    file = operation_with_file("../txtf/input_n3")
    print(check(input_f("../txtf/input_n3"),file))
    ins_sort = string(file)
    w_1 = write_s("../txtf/output_n3", ins_sort)
