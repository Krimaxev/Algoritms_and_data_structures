from lab_6.utils import read_file_one, check_first, write_one


def process_operations(operation):
    results = []
    my_set = set()

    for op in operation:
        if op.startswith('A'):
            _, x = op.split()
            x = int(x)
            my_set.add(x)
        elif op.startswith('D'):
            _, x = op.split()
            x = int(x)
            my_set.discard(x)
        elif op.startswith('?'):
            _, x = op.split()
            x = int(x)
            results.append('Y' if x in my_set else 'N')

    return results


if __name__=="__main__":
        FILE_INPUT = "../txtf/input.txt"
        FILE_OUTPUT = "../txtf/output.txt"
        file_i = read_file_one(FILE_INPUT)
        num_operations, operations = file_i[0], file_i[1]
        check = check_first(num_operations, operations)
        if check:
            result = process_operations(operations)
            write_one(FILE_OUTPUT, result)
            print("В файле src задания №1 ЛР №6 код работает исправно")
        else:
            write_one(FILE_OUTPUT, "ОШИБКА ВХОДНЫХ ДАННЫХ")
            raise ValueError("ОШИБКА ВХОДНЫХ ДАННЫХ")








