import random
matrix = [[random.randint(-50, 50) for _ in range(4)] for _ in range(4)]
negative_cells = [(i, j) for i in range(4) for j in range(4) if matrix[i][j] < 0]
print("Отрицательные в ячейках:", negative_cells)