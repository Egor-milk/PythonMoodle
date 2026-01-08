import random

n = 4
matrix = [[random.randint(-5, 5) for _ in range(n)] for _ in range(n)]

sum_below = sum(matrix[i][j] for i in range(n) for j in range(n) if i > j)
prod_above = 1
for i in range(n):
    for j in range(n):
        if i < j and matrix[i][j] != 0:
            prod_above *= matrix[i][j]

print("Матрица:", matrix)
print("Сумма ниже диагонали:", sum_below)
print("Произведение выше диагонали:", prod_above)