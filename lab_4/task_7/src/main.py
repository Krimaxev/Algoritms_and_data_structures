from collections import deque
from lab_4.utils import string, read_input_seven, check_seven, write_output

def max_dynamic_sequence(n,a,m):
    decart_queue = deque()
    result = []

    for i in range(n):
        if decart_queue and decart_queue[0] < i - m + 1:
            decart_queue.popleft()

        while decart_queue and a[decart_queue[-1]] <= a[i]:
            decart_queue.pop()

        decart_queue.append(i)

        if i >= m - 1:
            result.append(a[decart_queue[0]])

    return result

if __name__=="__main__":
    FILE_INPUT = "../txtf/input.txt"
    FILE_OUTPUT = "../txtf/output.txt"
    check = check_seven(FILE_INPUT)
    if check:
        argues = read_input_seven(FILE_INPUT)
        n, a, m = argues[0], argues[1], argues[2]
        result = max_dynamic_sequence(n, a, m)
        write_output(FILE_OUTPUT,string(result))
        print("Входные данные корректны")

    else:
        write_output(FILE_OUTPUT, "ОШИБКА ВХОДНЫХ ДАННЫХ")
        raise ValueError("ОШИБКА ВХОДНЫХ ДАННЫХ")









