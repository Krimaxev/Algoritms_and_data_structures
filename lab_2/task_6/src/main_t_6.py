from lab_2.utils import *

def max_subarray(list):

    max_profit = best_buy_price = best_sell_price = summs = 0

    for i in range(len(list)):
        if summs == 0: best_buy_price = min(list)
        summs += list[i]
        if max_profit < summs:
            max_profit = best_sell_price-best_buy_price
            best_sell_price = max(list)
        if summs < 0: summs = 0
    bbp, bsp, mp = best_buy_price, best_sell_price, max_profit
    v = [bbp,bsp,mp]
    return v

if __name__=="__main__":
    subarray_operation("../txtf/input_task_6","../txtf/output_task_6")