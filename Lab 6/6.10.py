import random

matrix = [[random.randint(0, 99) for _ in range(4)] for _ in range(4)]
total = sum(sum(row) for row in matrix)
print("Сумма всех элементов:", total)