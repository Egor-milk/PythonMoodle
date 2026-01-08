import random
n = 4
matrix = [[random.uniform(-2, 2) for _ in range(n)] for _ in range(n)]

# Элементы главной диагонали в [-1, 1]
diag_count = sum(1 for i in range(n) if -1 <= matrix[i][i] <= 1)

# Произведение ненулевых элементов последней строки
last_row = matrix[-1]
prod = 1
for x in last_row:
    if x != 0:
        prod *= x

print("Матрица:", matrix)
print("Элементов диагонали в [-1,1]:", diag_count)
print("Произведение последней строки:", prod)