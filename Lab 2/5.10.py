print('введите значения от x1 до x10 через пробел')
x = [float(i) for i in input().split()]

s = sum(map(lambda z: (z - 2) ** 3, x)) + sum(map(lambda z: z ** 2, x))
print(f'а = {s:.2f}')
