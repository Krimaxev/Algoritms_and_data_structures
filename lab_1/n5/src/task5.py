import sys
import time
import resource
time_start = time.perf_counter()
def Selection_sort(a):
    for i in range(0,len(a)-1):
        mn = i
        for j in range(i+1,len(a)):
            if a[j]<a[mn]:
                mn = j
        a[i],a[mn] = a[mn],a[i]
    return a
f,f2 = open("../txtf/input_n5", "r"),open("../txtf/output_n5", "w")
l,l2= int(f.readline()),f.readline()
m = [int(x) for x in l2.split()]

if l==0 or l>10**3: print("Лимит длины превышен")
if len(m)!=l: print("Ошибка")
for i in range(len(m)):
    if abs(m[i])>10**9: print("Ошибка")

t = Selection_sort(m)
s = ''
m1 = [str(x) for x in m]
for z in m1:
    s+=z
    s+=' '
f2.write(s)
f.close()
f2.close()
time_elapsed = (time.perf_counter() - time_start)
memMb=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024.0/1024.0
print("ВРЕМЯ:",time_elapsed)
print ("Память:%5.1f МБ" % (memMb))
print(f"Размер списка: {sys.getsizeof(m)} байт")
