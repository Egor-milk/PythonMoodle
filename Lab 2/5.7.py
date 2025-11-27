from math import tan, cos, sin, pi, log, e, sqrt

print('введите k, l через пробел')
k, l = [float(i) for i in input().split()]
t = ((k ** 2 - l ** 2) / (15 * k * l)) + ((1.5 * k + l) ** 3)
print(f't = {t:.2f}')
