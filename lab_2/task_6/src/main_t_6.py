from lab_2.utils import *

def max_subarray(prices, dates):
    if not prices or len(prices) != len(dates):
        return [0, 0, 0, None, None]

    min_price = float('inf')
    min_price_index = -1
    max_profit = 0
    best_buy_date = None
    best_sell_date = None

    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
            min_price_index = i

        potential_profit = prices[i] - min_price
        if potential_profit > max_profit and i > min_price_index :
            max_profit = potential_profit
            best_buy_index = min_price_index
            best_sell_index = i

    if max_profit > 0 and best_buy_index !=-1 and best_sell_index != -1:
        best_buy_price = prices[best_buy_index]
        best_sell_price = prices[best_sell_index]
        best_buy_date = dates[best_buy_index]
        best_sell_date = dates[best_sell_index]
        return [best_buy_price, best_sell_price, max_profit, best_buy_date, best_sell_date]
    else:
        return [0, 0, 0, None, None]

if __name__=="__main__":
    a = subarray_operation("../txtf/input_task_6","../txtf/output_task_6")
