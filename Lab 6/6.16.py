import random

matrix = [[random.randint(0, 99) for _ in range(4)] for _ in range(4)]
max_val = max(max(row) for row in matrix)

for i in range(4):
    for j in range(4):
        if matrix[i][j] == max_val:
            row_sum = sum(matrix[i])
            col_sum = sum(matrix[k][j] for k in range(4))
            print("Максимум в", (i, j))
            print("Сумма строки:", row_sum)
            print("Сумма столбца:", col_sum)