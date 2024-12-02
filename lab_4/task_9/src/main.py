from collections import deque
from lab_4.utils import read_input, check_nine, write_output, string_column

def process_requests(n, requests):
    queue = deque()
    results = []

    for request in requests:
        if request[0] == '+':

            _, i = request.split()
            queue.append(i)
        elif request[0] == '*':

            _, i = request.split()
            mid = (len(queue) + 1) // 2
            queue.insert(mid, i)
        elif request[0] == '-':

            results.append(queue.popleft())

    return results

if __name__=="__main__":
    FILE_INPUT = "../txtf/input.txt"
    FILE_OUTPUT = "../txtf/output.txt"
    check = check_nine(FILE_INPUT)
    if check:
        list = read_input(FILE_INPUT)
        write_output(FILE_OUTPUT,string_column(process_requests(list[1:],list)))
        print("Входные данные корректны")

    else:
        write_output(FILE_OUTPUT, "ОШИБКА ВХОДНЫХ ДАННЫХ")
        raise ValueError("ОШИБКА ВХОДНЫХ ДАННЫХ")







