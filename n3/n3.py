with open("fib2_input", "r") as f:
    for s in f:
        a = [int(x) for x in s.split()]

c = 0
x = a[0]
fb1 = fb2 = 1
while c < x - 2:
    if x < 0 or x > 10 ** 7:
        print("Ошибка")
        break
    else:
        fbs = fb1 + fb2
        fb1 = fb2
        fb2 = fbs
        c+=1
t = fb2%10

with open("fib2_output", "w") as z:
    z.write(str(t))
    z.close()






