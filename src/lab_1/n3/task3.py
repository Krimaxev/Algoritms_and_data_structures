import sys
import time
import resource
time_start = time.perf_counter()
def IS(a):
    for j in range(1,len(a)):
        u=j
        while u > 0 and a[u] > a[u-1]:
            a[u],a[j]=a[j],a[u]
            u = u - 1
    return a
f,f2 = open("input_n3","r"),open("output_n3","w")
l,l2= int(f.readline()),f.readline()
m = [int(x) for x in l2.split()]
if l==0 or l>10**3: print("Лимит длины превышен")
if l!=len(m): print("Ошибка")
for i in range(len(m)):
    if abs(m[i])>10**9: print("Ошибка")
t = IS(m)
s = ''
m1 = [str(x) for x in m]
for z in m1:
    s+=z
    s+=' '
f2.writelines(s)
f.close()
f2.close()
time_elapsed = (time.perf_counter() - time_start)
memMb=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024.0/1024.0
print("ВРЕМЯ:",time_elapsed)
print ("Память:%5.1f МБ" % (memMb))
print(f"Размер списка: {sys.getsizeof(m)} байт")