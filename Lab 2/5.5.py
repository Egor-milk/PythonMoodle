from math import tan, cos, sin, pi, log, e


print('введите a, b через пробел')
a, b = [float(i) for i in input().split()]

x = (a + b) * a

if a == b:
    y = x / (a * b)
else:
    y = (x ** 2) * (a - b)

if y <= 2:
    z = x / y
else:
    z = (a * b) / (x * y)
print(f'x = {x:.2f}, y = {y:.2f}, z = {z:.2f}')
