import sys
import time
import resource
time_start = time.perf_counter()

def insertion_sort(a):
    for j in range(len(a)):
        key = a[j]
        u = j-1
        while u>=0 and a[u]>key:
            a[u+1]=a[u]
            u = u-1
        a[u+1] = key

f,f2 = open("input_n1","r"),open("output_n1","w")
l,l2= int(f.readline()),f.readline()
m = [int(x) for x in l2.split()]

if l==0 or l>10**3: print("Лимит длины превышен")
if l!=len(m): print("Ошибка")
for i in range(len(m)):
    if abs(m[i])>10**9: print("Ошибка")

insertion_sort(m)
s = ''
m1 = [str(x) for x in m]
for z in m1:
    s+=z
    s+=' '
f2.write(s)

time_elapsed = (time.perf_counter() - time_start)
memMb=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024.0/1024.0
f.close()
f2.close()
print("ВРЕМЯ:",time_elapsed)
print ("Память:%5.1f МБ" % (memMb))
print(f"Размер списка: {sys.getsizeof(m)} байт")








