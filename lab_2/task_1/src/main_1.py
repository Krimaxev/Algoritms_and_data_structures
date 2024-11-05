from lab_2.utils import *

def merge(left_list, right_list):
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

def merge_sort(x):
    if len(x) <= 1:
        return x

    median_x = len(x) // 2
    left_list = merge_sort(x[:median_x])
    right_list = merge_sort(x[median_x:])
    return merge(left_list, right_list)


if __name__=="__main__":
    file = operation_with_file("../txtf/input_task_1")
    m1 = merge_sort(file)
    res = string(m1)
    output = output_file("../txtf/output_task_1", res)
    print(first_check(input_file_n("../txtf/input_task_1"),operation_with_file("../txtf/input_task_1")))


