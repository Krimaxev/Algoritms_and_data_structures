import time

start = time.time()
import resource

time_start = time.perf_counter()

f, f2 = open("../txtf/input_n4", "r"), open("../txtf/output_n4", "w")
l, l2 = f.readline(), int(f.readline())
m = [int(x) for x in l.split()]

if len(m) > 10 ** 3: print("Лимит длины превышен")
for j in range(len(m)):
    if m[j] < -10 ** 3 or m[j] > 10 ** 3: print("Ошибка")
if l2 < -10 ** 3 or l2 > 10 ** 3: print("Лимит значения превышен")

m1 = [x for x, y in enumerate(m) if y == l2]

str_count = str(len(m1))
s = ''
for k in range(len(m1)):
    if len(m1) == 1:
        f2.write(str(m1[k]))
    else:
        s += str(m1[k])
        s += ', '
if len(m1) == 0:
    f2.write("-1")

else:
    f2.write(str_count + '\n')
    f2.write(s[:-2])
f.close()
f2.close()
time_elapsed = (time.perf_counter() - time_start)
memMb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024.0
print("ВРЕМЯ:", time_elapsed)
print("Память:%5.1f МБ" % (memMb))
