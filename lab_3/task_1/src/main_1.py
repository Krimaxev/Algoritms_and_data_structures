import random
import heapq
from lab_3.utils import input_operation, output_operation, first_check, string


def three_way_partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = low + 1
    k = high

    while j <= k:
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j += 1
        elif arr[j] > pivot:
            arr[j], arr[k] = arr[k], arr[j]
            k -= 1
        else:
            j += 1
    arr[low], arr[i-1] = arr[i-1], arr[low]
    return i - 1, k

def partition(arr, low, high):
    pivot_index = random.randint(low, high)
    pivot = arr[pivot_index]
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort_threeway(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        mid1, mid2 = three_way_partition(arr, low, high)
        quicksort_threeway(arr, low, mid1 - 1)
        quicksort_threeway(arr, mid2 + 1, high)

def quicksort_standard(arr, low=0, high=None, max_depth=None):
    if high is None:
        high = len(arr) - 1
    if max_depth is None:
        max_depth = 2 * len(arr).bit_length()

    if low < high:
        if max_depth <= 0:
            heapq.heapify(arr[low:high+1])
            for i in range(high, low -1, -1):
              arr[i], arr[low] = arr[low], arr[i]
              heapq.heapify(arr[low:i])
        else:
            pivot_index = partition(arr, low, high)
            quicksort_standard(arr, low, pivot_index - 1, max_depth - 1)
            quicksort_standard(arr, pivot_index + 1, high, max_depth - 1)

if __name__=="__main__":
    input_f = "../txtf/input"
    output_f = "../txtf/output"
    input_f2 = "../txtf/hard_input"
    output_f2 = "../txtf/hard_output"
    FIRST_CHECK_1 = first_check("../txtf/input")
    FIRST_CHECK_2 = first_check("../txtf/hard_input")
    if FIRST_CHECK_1:
        result = input_operation(input_f)
        quicksort_threeway(result)
        output_operation(output_f, string(result))
        print("В файле src задания №1 ЛР №3 код работает исправно")
    else:
        output_operation(output_f, "Ошибка входных данных")
        print(f"Ошибка входных данных в файле: {input_f}")

    if FIRST_CHECK_2:
        result2 = input_operation(input_f2)
        quicksort_threeway(result2)
        output_operation(output_f2, string(result2))

    else:
        output_operation(output_f2, "Ошибка входных данных")
        print(f"Ошибка входных данных в файле: {input_f2}")
























