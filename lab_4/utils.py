
def read_input(a):
    f = open(a, "r")
    f1 = int(f.readline())
    f2 = f.readlines()
    res = [x.rstrip() for x in f2]
    return res

def read_input_seven(a):
    f = open(a,"r")
    n = int(f.readline())
    arr = [int(x) for x in f.readline().split()]
    m = int(f.readline())
    return n, arr, m

def write_output(a,b):
    f = open(a,"w")
    f.write(str(b))

def string(a):
    s = ''
    for i in range(len(a)):
        s+=str(a[i])
        s+=' '
    return s[:-1]

def string_column(a):
    s = ''
    for i in range(len(a)):
        s+=a[i]+"\n"
    return s

def check(a):
    f = open(a, "r")
    f1 = int(f.readline())
    list = read_input(a)

    if f1==0 or f1> 10**6:
        return False

    if f1 != len(list):
        return False

    return True

def check_three(a):
    f = open(a, "r")
    f1 = int(f.readline())
    list = read_input(a)

    if f1 == 0 or f1 > 500:
        return False

    if f1 != len(list):
        return False

    for i in range(len(list)):
        if not(1<=len(list[i])<=10**4):
            return False

    return True


def check_five(a):
    with open(a, "r") as f:
        lines = f.readlines()
    try:
        f1 = int(lines[0].strip())
    except (ValueError, IndexError):
        return False


    if not (1 <= f1 <= (40 * 10 ** 4)):
        return False


    str_numbers = []
    for line in lines[1:]:
        digit_only = "".join(char for char in line if char.isdecimal())
        str_numbers.append(digit_only)

    numbers = [int(char) for char in str_numbers if char.isdigit()]

    for i in range(len(numbers)):
        if not(0<=numbers[i]<=10**5):
            return False
    return True

def check_seven(a):
    elements = read_input_seven(a)
    n,a,m = elements[0], elements[1], elements[2]

    if not(1<=n<=10**5):
        return False

    if not(1<=m<=m):
        return False

    for i in range(len(a)):
        if not(0<=a[i]<=10**5):
            return False

    return True

def check_nine(a):
    f = open(a, "r")
    f1 = int(f.readline())
    list = read_input(a)

    if not(1<=f1<=10**5):
        return False

    if len(list)!=f1:
        return False

    return True




















