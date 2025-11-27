import math

print('Введите радиус основания 1, радиус основания 2, высоту')
r1, r2, h = map(float, input().split())
l = math.hypot(h, r1 - r2)
print(f'Площадь поверхности: {(math.pi * (r1*r1 + r2*r2 + (r1 + r2)*l)):.2f}\n'
      f'Объем: {(math.pi * (r1 + r2) * l + math.pi * (r1*r1 + r2*r2)):.2f}')