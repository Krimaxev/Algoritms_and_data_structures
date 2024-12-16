from collections import deque
from lab_5.utils import input_operation_task_three, check_third_task, output_operation, string_lab_five


def process_packets(buffer_size, packet):
    finish_time = deque()
    result = []

    for arrival, processing in packet:
        while finish_time and finish_time[0] <= arrival:
            finish_time.popleft()

        if len(finish_time) < buffer_size:
            start_time = max(arrival, finish_time[-1] if finish_time else 0)
            finish_time.append(start_time + processing)
            result.append(start_time)
        else:
            result.append(-1)

    return string_lab_five(result)


if __name__=="__main__":
    FILE_INPUT = "../txtf/input.txt"
    FILE_OUTPUT = "../txtf/output.txt"
    input_f = input_operation_task_three(FILE_INPUT)
    n, buf_size, packets = input_f[0], input_f[1], input_f[2]
    check = check_third_task(n, buf_size)
    if check:
        results = process_packets(buf_size, packets)
        output_operation(FILE_OUTPUT, results)
        print("В файле src задания №3 ЛР №5 код работает исправно")
    else:
        output_operation(FILE_OUTPUT, "ОШИБКА ВХОДНЫХ ДАННЫХ")
        raise ValueError("ОШИБКА ВХОДНЫХ ДАНННЫХ")

