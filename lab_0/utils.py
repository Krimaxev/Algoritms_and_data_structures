
def check_one(a,b):
    if (not(abs(a)<=10**9)) or (not(abs(b)<=10**9)):
        return False
    return True

def check_two(n):
    if n==0:
        return False
    if n<0 or n>45:
        return False
    return True

def check_three(a):
    if not(0<=a<=10**7):
        return False
    return True

def read_file(a):
    f = open(a, "r")
    m = [int(x) for x in f.readline().split()]
    return m

def read_file_three(a):
    f = open(a, "r")
    n = int(f.readline())
    return n

def write_file(a, result):
    f = open(a, "w")
    f.write(str(result))