import random

matrix = [[random.randint(0, 99) for _ in range(5)] for _ in range(5)]
sorted_matrix = [sorted(row) for row in matrix]
print("Отсортированные строки:", sorted_matrix)