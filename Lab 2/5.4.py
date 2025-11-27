from math import tan, cos, sin, pi, log, e


print('введите x, y, z через пробел')
x, y, z = [float(i) for i in input().split()]

a = cos(log(x)) / log(y)
b = (1 / (z + ((x ** 2 )/ (y + z)))) + e ** z

print(f'а = {a:.2f}, b = {b:.2f}')
