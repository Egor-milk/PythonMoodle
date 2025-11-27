import math

# Ввод данных для трапеции
print("Введите параметры равнобедренной трапеции:")
a = float(input("Длина большего основания (см): "))
b = float(input("Длина меньшего основания (см): "))
c = float(input("Длина боковой стороны (см): "))
angle = float(input("Угол при основании в градусах: "))
height = float(input("Высота трапеции (см): "))

# Способ 1: через стороны и угол
angle_rad = math.radians(angle)
height_from_angle = c * math.sin(angle_rad)
area1 = (a + b) * height_from_angle / 2

# Способ 2: через основания и высоту
area2 = (a + b) * height / 2

# Вывод результатов
print(f"\nРезультаты вычислений:")
print(f"Способ 1 (через стороны и угол):")
print(f"  Вычисленная высота: {height_from_angle:.2f} см")
print(f"  Площадь: {area1:.2f} см²")

print(f"Способ 2 (через основания и высоту):")
print(f"  Площадь: {area2:.2f} см²")

# Сравнение результатов
print(f"\nРазница между способами: {abs(area1 - area2):.4f} см²")