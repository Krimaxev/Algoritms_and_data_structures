from lab_6.utils import read_file_one, check_four, write_one, read_file_four


class SuffixMap:
    def __init__(self):
        self.data = {}
        self.order = []

    def put(self, x, y):
        if x not in self.data:
            self.order.append(x)
        self.data[x] = y

    def get(self, x):
        return self.data.get(x, "<none>")

    def prev(self, x):
        if x not in self.data:
            return "<none>"
        index = self.order.index(x)
        return self.data[self.order[index - 1]] if index > 0 else "<none>"

    def next(self, x):
        if x not in self.data:
            return "<none>"
        index = self.order.index(x)
        return self.data[self.order[index + 1]] if index < len(self.order) - 1 else "<none>"

    def delete(self, x):
        if x in self.data:
            del self.data[x]
            self.order.remove(x)


def execute_operations(operations):
    suffix_map = SuffixMap()
    results = []

    for operation in operations:
        cmd = operation[0]
        if cmd == 'put':
            suffix_map.put(operation[1], operation[2])
        elif cmd == 'get':
            results.append(suffix_map.get(operation[1]))
        elif cmd == 'prev':
            results.append(suffix_map.prev(operation[1]))
        elif cmd == 'next':
            results.append(suffix_map.next(operation[1]))
        elif cmd == 'delete':
            suffix_map.delete(operation[1])

    return results


if __name__=="__main__":
    FILE_INPUT = "../txtf/input.txt"
    FILE_OUTPUT = "../txtf/output.txt"
    file_i = read_file_one(FILE_INPUT)
    num_operations = file_i[0]
    operation = read_file_four(FILE_INPUT)
    check = check_four(num_operations, operation)
    if check:
        result = execute_operations(operation)
        write_one(FILE_OUTPUT, result)
        print("В файле src задания №4 ЛР №6 код работает исправно")
    else:
        write_one(FILE_OUTPUT, "ОШИБКА ВХОДНЫХ ДАННЫХ")
        raise ValueError("ОШИБКА ВХОДНЫХ ДАННЫХ")







