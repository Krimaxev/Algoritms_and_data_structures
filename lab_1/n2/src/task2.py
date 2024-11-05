import sys
import time
import resource
time_start = time.perf_counter()
f,f2 = open("../txtf/input_n2", "r"),open("../txtf/output_n2", "w")
l,l2= int(f.readline()),f.readline()
m = [int(x) for x in l2.split()]
m2 = []
if l!=len(m): print("Ошибка")
for j in range(len(m)):
    key = m[j]
    u = j - 1
    while u >= 0 and m[u] > key:
        m[u + 1] = m[u]
        u = u - 1
    m[u + 1] = key
    m2.append(m.index(key))
s = ''
s1 = ''
m1 = [str(x) for x in m]
m3 = [str(x+1) for x in m2]
for z in m1:
    s+=z
    s+=' '
for p in m3:
    s1+=p
    s1+=' '
f2.writelines(s1+"\n")
f2.writelines(s)
f.close()
f2.close()
time_elapsed = (time.perf_counter() - time_start)
memMb=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024.0/1024.0
print("ВРЕМЯ:",time_elapsed)
print ("Память:%5.1f МБ" % (memMb))
print(f"Размер списка: {sys.getsizeof(m)} байт")
