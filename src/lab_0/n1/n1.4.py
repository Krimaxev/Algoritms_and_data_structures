with open("input.txt", "r") as f:
    for s in f:
        a1 = [int(x) for x in s.split()]
        a,b = a1[0],a1[1]
        t = a+b**2

with open("output.txt", "w") as z:
    if -10**9 <= a <= 10**9 and -10**9 <= b <= 10**9:
        z.write(str(t))
    else: z.write("Ошибка")
    z.close()