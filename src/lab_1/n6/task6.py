import sys
import time
import resource
time_start = time.perf_counter()

def Bubble_sort(a):
    for i in range(1,len(a)-1):
        for j in range(len(a),i+1):
            if a[j]<a[j-1]:
                a[j],a[j-1] = a[j-1],a[j]
                return a


f,f2 = open("input_n6","r"),open("output_n6","w")
l,l2= int(f.readline()),f.readline()
m = [int(x) for x in l2.split()]

if l==0 or l>10**3: print("Лимит длины превышен")
if len(m)!=l: print("Ошибка")
for i in range(len(m)):
    if abs(m[i])>10**9: print("Ошибка")

t = Bubble_sort(m)
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

