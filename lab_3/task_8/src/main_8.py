from lab_3.utils import read_input, write_output, eighth_check, output_operation
import math

def closest_points(points, k):
    distances = []

    for point in points:
        if isinstance(point, tuple) and len(point) == 2:
            x, y = point
            distance = math.sqrt(x ** 2 + y ** 2)
            distances.append((distance, point))
        else:
            raise ValueError("Каждая точка должна быть кортежем с двумя координатами.")

    distances.sort(key=lambda x: x[0])
    return [point for _, point in distances[:k]]

if __name__ == "__main__":
    FILE_INPUT = "../txtf/input"
    FILE_OUTPUT = "../txtf/output"
    points, k = read_input(FILE_INPUT)
    point_check = eighth_check(FILE_INPUT)
    if point_check:
        result = closest_points(points, k)
        write_output(FILE_OUTPUT, result)
        print("В файле src задания №8 ЛР №3 код работает исправно")
    else:
        output_operation(FILE_OUTPUT, "Ошибка входных данных")
        print("Ошибка входных данных")










