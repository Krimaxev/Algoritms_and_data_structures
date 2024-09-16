m = []
with open("../../Library/Application Support/JetBrains/PyCharmCE2024.2/scratches/input.txt", "r") as f:
    for s in f: m.append(sum([int(x) for x in s.split()]))

with open("../../Library/Application Support/JetBrains/PyCharmCE2024.2/scratches/output.txt", "w") as z:
    z.write(str(m[0]))
    z.close()




