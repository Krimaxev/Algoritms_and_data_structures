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
    INPUT_FILE = "../txtf/test_1_input"
    OUTPUT_FILE = "../txtf/test_1_output"

    data = read_input(INPUT_FILE)
    if data:
        sorted_data = merge_sort(data)
        write_output(output_file, sorted_data)

    print(first_check(input_file_n(INPUT_FILE),operation_with_file(INPUT_FILE)))


