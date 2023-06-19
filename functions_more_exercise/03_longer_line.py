from math import sqrt
from math import floor

def closest_to_center_of_coordinate(a, b, c, d):
    distance_a = sqrt(a ** 2 + b ** 2)
    distance_b = sqrt(c ** 2 + d ** 2)
    if distance_a <= distance_b:
        result = f"({floor(a)}, {floor(b)})({floor(c)}, {floor(d)})"
    else:
        result = f"({floor(c)}, {floor(d)})({floor(a)}, {floor(b)})"
    return result


def length_of_line(x1, y1, x2, y2):
    if x1 > 0 and x2 > 0:
        side_a = abs(x1) - abs(x2)
    else:
        side_a = abs(x1) + abs(x2)

    if y1 > 0 and y2 > 0:
        side_b = abs(y1) - abs(y2)
    else:
        side_b = abs(y1) + abs(y2)

    length = sqrt(side_a ** 2 + side_b ** 2)
    return length

x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())
x3, y3, x4, y4 = float(input()), float(input()), float(input()), float(input())

line_a = length_of_line(x1, y1, x2, y2)
# print(line_a)
line_b = length_of_line(x3, y3, x4, y4)
# print(line_b)

if line_a >= line_b:
    print(closest_to_center_of_coordinate(x1, y1, x2, y2))
else:
    print(closest_to_center_of_coordinate(x3, y3, x4, y4))
