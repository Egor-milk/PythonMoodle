from math import tan, cos, sin, pi, log, e, sqrt


print('введите x, y, z через пробел')
x, y, z = [float(i) for i in input().split()]

a = sqrt(abs(x - 1)) - (y ** (1. / 3.))
b = (x * (tan(z) + (e ** (-x)))) / (x - (((x - 1) ** (y ** (1 / sin(z)))) / ((y ** 3) + 3 * (x + y))))

print(f'а = {a:.2f}, b = {b:.2f}')
