def Max_subarray(list):

    max_profit = best_buy_price = best_sell_price = summs = 0

    for i in range(len(list)):
        if summs == 0:
            best_buy_price = min(list)
        summs += list[i]
        if max_profit < summs:
            max_profit = best_sell_price-best_buy_price
            best_sell_price = max(list)
        if summs < 0:
            summs = 0
    bbp, bsp, mp = best_buy_price, best_sell_price, max_profit
    v = [bbp,bsp,mp]
    return v

if __name__=="__main__":
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

    f1.close()
    f2.close()