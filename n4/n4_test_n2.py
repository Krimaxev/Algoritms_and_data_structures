import time
t_start = time.time()

with open("n4_input_n2", "r") as f:
    for s in f:
        a = [int(x) for x in s.split()]
        n = a[0]

fb1 = fb2 = 1
for i in range(2,n):
    fb1,fb2 = fb2,fb1+fb2
t = str(fb2)

with open("n4_output_n2", "w") as z:
    if 0<=n<=45:
        z.write(str(t))
        print(time.time() - t_start)
    else: print("Ошибка")
    z.close()

