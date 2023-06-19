from math import sqrt
from math import floor

def coordinate_system(x, y):
    distance = sqrt(x ** 2 + y ** 2)
    return distance


x1 = float(input())
y1 = float(input())
distance_one = coordinate_system(x1, y1)
x2 = float(input())
y2 = float(input())
distance_two = coordinate_system(x2, y2)
if distance_one < distance_two:
    print(f"({floor(x1)}, {floor(y1)})")
else:
    print(f"({floor(x2)}, {floor(y2)})")
