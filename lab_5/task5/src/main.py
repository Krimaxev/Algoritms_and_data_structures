import heapq
from lab_5.utils import input_operation_task_five, check_five_task, output_operation_five, output_operation


def job_scheduler(num_p, job):
    heap = [(0, i) for i in range(num_p)]
    results = []

    for duration in job:
        finish_time, thread = heapq.heappop(heap)
        results.append((thread, finish_time))
        heapq.heappush(heap, (finish_time + duration, thread))

    return results

if __name__=="__main__":
    FILE_INPUT = "../txtf/input.txt"
    FILE_OUTPUT = "../txtf/output.txt"
    input_f = input_operation_task_five(FILE_INPUT)
    n, m, jobs = input_f[0], input_f[1], input_f[2]
    check = check_five_task(n, m, jobs)
    if check:
        result = job_scheduler(n, jobs)
        output_operation_five(FILE_OUTPUT,result)
        print("В файле src задания №5 ЛР №5 код работает исправно")
    else:
        output_operation(FILE_OUTPUT,"ОШИБКА ВХОДНЫХ ДАННЫХ")
        raise ValueError("ОШИБКА ВХОДНЫХ ДАННЫХ")