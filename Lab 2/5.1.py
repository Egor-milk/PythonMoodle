from math import tan


print('введите x, y, z через пробел')
x, y, z = [float(i) for i in input().split()]

a = (5 * (tan(x))) - (2 * tan(y))
b = (tan(y-z)) / (y-x) / (1 + ((y - x) ** 2))

print(f'а = {a:.2f}, b = {b:.2f}')