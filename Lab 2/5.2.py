from math import tan, cos, sin, pi, fabs


print('введите x, y, z через пробел')
x, y, z = [float(i) for i in input().split()]

a = (2 * cos(x - (pi / 6))) / (sin(y + 1 / z) ** 2)
b = (z ** 2) / (3 - fabs(y)) + 1

print(f'а = {a:.2f}, b = {b:.2f}')
