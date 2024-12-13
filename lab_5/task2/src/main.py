from lab_5.utils import check_second_task, input_operation, output_operation

def compute_tree_height(n, parents):
    depth = [0] * n

    def find_depth(node):
        if depth[node] != 0:
            return depth[node]
        if parents[node] == -1:
            depth[node] = 1
        else:
            depth[node] = find_depth(parents[node]) + 1
        return depth[node]


    for i in range(n):
        find_depth(i)

    return max(depth)

if __name__=="__main__":
    FILE_INPUT = "../txtf/input.txt"
    OUTPUT_FILE = "../txtf/output.txt"
    input_f = input_operation(FILE_INPUT)
    length_line, PARENTS = input_f[0], input_f[1]
    check = check_second_task(length_line,PARENTS)
    if check:
        result = compute_tree_height(length_line,PARENTS)
        output_operation(OUTPUT_FILE,result)
        print("Входные данные корректны")
    else:
        output_operation(OUTPUT_FILE, "ОШИБКА ВХОДНЫХ ДАННЫХ")
        raise ValueError("ОШИБКА ВХОДНЫХ ДАННЫХ")
