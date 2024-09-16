
with open("../../Library/Application Support/JetBrains/PyCharmCE2024.2/scratches/input.txt", "r") as f:
    for s in f:
        a = [int(x) for x in s.split()]
        t = a[0]+a[1]**2
with open("../../Library/Application Support/JetBrains/PyCharmCE2024.2/scratches/output.txt", "w") as z:
    z.write(str(t))
    z.close()