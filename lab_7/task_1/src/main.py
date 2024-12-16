from lab_7.utils import read_file_coins, check_money, write_file


def min_change(coin, total):
    counts = [0] * (total + 1)
    counts[0] = 0
    maximum = float('inf') - 1
    for i in range(1, total + 1):
        count = maximum
        for j in range(len(coin)):
            if i - coin[j] >= 0 and count > counts[i - coin[j]]:
                count = counts[i - coin[j]]
        if count < maximum:
            counts[i] = count + 1
        else:
            counts[i] = maximum
    return counts[total]



if __name__=="__main__":
    FILE_INPUT = "../txtf/input.txt"
    FILE_OUTPUT = "../txtf/output.txt"
    file_i = read_file_coins(FILE_INPUT)
    money, coins, k = file_i[0], file_i[1], file_i[2]
    check = check_money(money, k, coins)
    if check:
        result = min_change(coins, money)
        write_file(FILE_OUTPUT, result)
        print("В файле src задания №1 ЛР №7 код работает исправно")
    else:
        write_file(FILE_OUTPUT, "ОШИБКА ВХОДНЫХ ДАННЫХ")
        raise ValueError("ОШИБКА ВХОДНЫХ ДАННЫХ")





