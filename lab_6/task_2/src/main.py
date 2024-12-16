from lab_6.utils import read_file_one, check_second, write_one


def phone_book_manager(lines):

    queries = [line.strip().split() for line in lines[1:]]

    phone_book = {}
    results = []

    for query in queries:
        command = query[0]
        number = query[1]

        if command == 'add':
            name = query[2]
            phone_book[number] = name
        elif command == 'del':
            phone_book.pop(number, None)
        elif command == 'find':
            if number in phone_book:
                results.append(phone_book[number])
            else:
                results.append('not found')

    return results

if __name__=="__main__":
    FILE_INPUT = "../txtf/input.txt"
    FILE_OUTPUT = "../txtf/output.txt"
    file_i = read_file_one(FILE_INPUT)
    num_call, calls = file_i[0], file_i[1]
    check = check_second(num_call, calls)
    if check:
        result = phone_book_manager(calls)
        write_one(FILE_OUTPUT, result)
        print("В файле src задания №2 ЛР №6 код работает исправно")
    else:
        write_one(FILE_OUTPUT, "ОШИБКА ВХОДНЫХ ДАННЫХ")
        raise ValueError("ОШИБКА ВХОДНЫХ ДАННЫХ")



