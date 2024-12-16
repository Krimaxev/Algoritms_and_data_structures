from lab_2.utils import read_input, write_output, string, output_file

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
    INPUT_FILE = "../txtf/input_task_1"
    OUTPUT_FILE = "../txtf/output_task_1"

    data = read_input(INPUT_FILE)
    if data:
        sorted_data = string(merge_sort(data))
        write_output(OUTPUT_FILE, sorted_data)
        print("В файле src задания №1 ЛР №2 код работает исправно")



