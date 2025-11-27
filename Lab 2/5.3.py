from math import tan, cos, sin, pi, sqrt


print('введите m, n, p через пробел')
m, n, p = [float(i) for i in input().split()]

x1 = (m ** 2 + n - sqrt(abs(m * p))) / 10
if 10 < m < 15:
    x2 = m + n
else:
    x2 = p - m

print(f'x1 = {x1:.2f}, x2 = {x2:.2f}')