def LF(x):
    if x==0: return 1
    fb1,fb2 = 0,1
    for i in range(x-1):
        fb = (fb1+fb2)%10
        fb1,fb2 = fb2,fb
    return fb2

with open("fib2_input", "r") as f:
    for s in f:
        a = [int(x) for x in s.split()]

t = a[0]
if t<0 or t>10**7: print("Ошибка")
t2 = LF(t)

with open("fib2_output", "w") as z:
    z.write(str(t2))
    z.close()






