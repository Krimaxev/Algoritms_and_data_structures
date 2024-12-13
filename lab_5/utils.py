

def input_operation(file):
    f = open(file, "r")
    len_line = int(f.readline())
    line = [int(x) for x in f.readline().split()]
    return len_line,line

def input_operation_task_three(file):
    with open(file, "r") as f:
        buffer_size, n = map(int, f.readline().split())
        packets = [tuple(map(int, f.readline().split())) for _ in range(n)]
    return n, buffer_size, packets

def input_operation_task_five(file):
    with open(file, "r") as f:
        n, m = map(int, f.readline().split())
        jobs = list(map(int, f.readline().split()))
    return n, m, jobs

def output_operation_three(file,result):
    with open(file, "w") as f:
        f.write("\n".join(map(str, result)) + "\n")

def output_operation_five(file, result):
    with open(file, "w") as file:
        for thread, start_time in result:
            file.write(f"{thread} {start_time}\n")

def output_operation(file_o, result):
    f = open(file_o,"w")
    f.write(str(result))

def string_lab_five(a):
    s = ""
    for i in range(len(a)):
        s+=str(a[i])+"\n"
    return s

def check_first_task(len_line, line):
    if not(1<=len_line<=10**6):
        return False
    if len_line != len(line):
        return False
    for i in range(len(line)):
        if not(abs(line[i])<=(2*10**9)):
            return False
    return True

def check_second_task(len_line, line):
    if not(1<=len_line<=10**5):
        return False
    if len_line != len(line):
        return False
    for i in range(len(line)):
        if not(line[i]<=(len_line - 1)):
            return False
    return True

def check_third_task(n, buffer_size):
    if (not(1<=buffer_size<=10**5)) or (not(1<=n<=10**5)):
        return False
    return True

def check_five_task(n, m, t):
    if (not(1<=n<=10**5)) or (not(1<=m<=10**5)):
        return False
    if m != len(t):
        return False
    for i in range(len(t)):
        if not(0<=t[i]<=10**9):
            return False
    return True



