from lab_3.utils import open_f, string, output_operation, second_check

import random

def generate_worst_case(n):
    permutation = list(range(1, n + 1))
    random.shuffle(permutation)
    for i in range(n // 2):
        if random.random() < 0.5:
            permutation[i], permutation[n - 1 - i] = permutation[n - 1 - i], permutation[i]

    return permutation

if __name__ == "__main__":
    n = "../txtf/input"
    t = open_f(n)
    if second_check(t) == "Входное значение корректно":
        worst_case_permutation = generate_worst_case(t)
        res = string(worst_case_permutation)
        output_operation("../txtf/output",res)
        print("Входное значение корректно")
    else:
        print("Входное значение некорректно")