from math import tan, cos, sin, pi, log, e, sqrt


print('введите x, y, z через пробел')
x, y, z = [float(i) for i in input().split()]

a = sqrt(abs(x + (y ** 2) + z))
if a > 2:
    n = (x ** 2) - (y ** 3) + (2 * x * y)
elif a == 2:
    n = y ** 3 - x ** 2
else:
    n = 1 - ((y - z) / y + z)

print(f'а = {a:.2f}, n = {n:.2f}')
