from lab_2.task_6.src.main_t_6 import *
import sys
import time
import resource

if __name__=="__main__":
    time_start = time.perf_counter()
    f1,f2 = open("../txtf/input_task_6", "r"), open("../txtf/output_task_6", "w")
    l = f1.readline()
    price,date = [], []
    for s in f1:
        c = 0
        a = [x for x in s.split()]
        c+=1
        price.append(float(a[1]))
        date.append(a[0])
    t = Max_subarray(price)
    min_i, max_i = price.index(t[0]), price.index(t[1])
    buy_price, sell_price, profit = t[0], t[1], t[2]
    f2.write("Yandex\n"
             "Change period: 1 month\n"
             f"Date of purchase: {date[min_i]} Purchase price: {buy_price}\n"
             f"Date of sale: {date[max_i]} Sale price: {sell_price}\n"
             f"Profit: {profit}")

    time_elapsed = (time.perf_counter() - time_start)
    memMb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024.0
    print("ВРЕМЯ:", time_elapsed)
    print("Память:%5.1f МБ" % (memMb))
    print(f"Размер списка цен: {sys.getsizeof(price)} байт")
    print(f"Размер списка дат: {sys.getsizeof(date)} байт")
    f1.close()
    f2.close()