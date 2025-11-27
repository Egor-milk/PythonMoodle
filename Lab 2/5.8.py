from math import tan, cos, sin, pi, log, e, sqrt


print('введите x, y, z через пробел')
x, y, z = [float(i) for i in input().split()]

a = (y ** 3) * sqrt(abs(x)) + cos(y - 3)
b = (y * (tan(z) + (pi / 6))) / (abs(x) + (1 / ((y ** 2) + 1)))

print(f'а = {a:.2f}, b = {b:.2f}')
