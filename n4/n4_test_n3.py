import time
t_start = time.time()
with open("../../Library/Application Support/JetBrains/PyCharmCE2024.2/scratches/n4_input_n3", "r") as f:
    for s in f:
        a = [int(x) for x in s.split()]

x = a[0]
fb1 = fb2 = 1
for i in range(2,x):
    fb1,fb2 = fb2,fb1+fb2
    t = str(fb2)
    t2 = t[-1]

with open("../../Library/Application Support/JetBrains/PyCharmCE2024.2/scratches/n4_output_n3", "w") as z:
    z.write(t2)
    z.close()
print(time.time()-t_start)