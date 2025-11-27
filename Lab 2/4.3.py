from math import pi


print('Введите высоту, радиус, образующую конуса конуса через пробел')
h, r, l = [int(i) for i in input().split()]
print(f'Объем конуса равен {((1 / 3) * pi * r ** 2 * h):.2f}')
print(f'Площадь конуса равна {((pi * r * l) + (pi * r ** 2)):.2f}')