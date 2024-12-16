from lab_3.utils import nine_check, output_operation, read_input_n
import math

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def strip_closest(strip, d_min):
    min_d = d_min
    strip.sort(key=lambda point: point[1])
    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            if strip[j][1] - strip[i][1] >= min_d:
                break
            min_d = min(min_d, distance(strip[i], strip[j]))
    return min_d

def closest_pair_recursive(points):
    if len(points) <= 3:
        min_d = float('inf')
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                min_d = min(min_d, distance(points[i], points[j]))
        return min_d

    mid = len(points) // 2
    mid_x = points[mid][0]

    left_half = points[:mid]
    right_half = points[mid:]

    d_left = closest_pair_recursive(left_half)
    d_right = closest_pair_recursive(right_half)

    d_min = min(d_left, d_right)

    strip = [point for point in points if abs(point[0] - mid_x) < d_min]

    return min(d_min, strip_closest(strip, d_min))

def closest_pair(points):
    points.sort()
    return closest_pair_recursive(points)


if __name__ == "__main__":
    FILE_INPUT = "../txtf/input"
    FILE_OUTPUT = "../txtf/output"
    points = read_input_n(FILE_INPUT)
    point_check = nine_check(FILE_INPUT)
    if point_check:
        result = closest_pair(points)
        output_operation(FILE_OUTPUT, result)
        print("В файле src задания №9 ЛР №3 код работает исправно")
    else:
        output_operation(FILE_OUTPUT, "Ошибка входных данных")
        print("Ошибка входных данных")