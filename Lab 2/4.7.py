import math

# Ввод данных цилиндра
radius = float(input("Введите радиус основания цилиндра (см): "))
height = float(input("Введите высоту цилиндра (см): "))

# Вычисление площади поверхности и объема
base_area = math.pi * radius ** 2  # площадь основания
side_area = 2 * math.pi * radius * height  # площадь боковой поверхности
surface_area = 2 * base_area + side_area  # полная площадь поверхности
volume = base_area * height  # объем

# Вывод результатов
print(f"\nРезультаты вычислений для цилиндра:")
print(f"Радиус: {radius:.2f} см")
print(f"Высота: {height:.2f} см")
print(f"Площадь поверхности: {surface_area:.2f} см²")
print(f"Объем: {volume:.2f} см³")