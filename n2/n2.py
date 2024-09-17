def Fchi(x):
    if x<=1: return x
    return Fchi(x-1) + Fchi(x-2)

with open("../../Library/Application Support/JetBrains/PyCharmCE2024.2/scratches/fib_input", "r") as f:
    for s in f:
        a = [int(x) for x in s.split()]
        t = Fchi(a[0])

with open("../../Library/Application Support/JetBrains/PyCharmCE2024.2/scratches/fib_output", "w") as z:
    z.write(str(t))
    z.close()
