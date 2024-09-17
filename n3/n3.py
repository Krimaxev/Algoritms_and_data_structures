with open("../../Library/Application Support/JetBrains/PyCharmCE2024.2/scratches/fib2_input", "r") as f:
    for s in f:
        a = [int(x) for x in s.split()]

x = a[0]
fb1 = fb2 = 1
for i in range(2,x):
    fb1,fb2 = fb2,fb1+fb2
    t = str(fb2)
    t2 = t[-1]

with open("../../Library/Application Support/JetBrains/PyCharmCE2024.2/scratches/fib2_output", "w") as z:
    z.write(t2)
    z.close()

