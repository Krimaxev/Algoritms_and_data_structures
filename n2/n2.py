with open("fib_input", "r") as f:
    for s in f:
        a = [int(x) for x in s.split()]
        n = a[0]

fb1 = fb2 = 1
for i in range(2,n):
    fb1,fb2 = fb2,fb1+fb2
t = str(fb2)

with open("fib_output", "w") as z:
    if 0<=n<=45: z.write(str(t))
    else: print("Ошибка")
    z.close()
