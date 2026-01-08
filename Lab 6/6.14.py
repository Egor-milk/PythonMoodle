import random
n = 4
matrix = [[random.uniform(-10, 10) for _ in range(n)] for _ in range(n)]
main_diag = [matrix[i][i] for i in range(n)]
side_diag = [matrix[i][n-1-i] for i in range(n)]

print("Матрица:", matrix)
print("Главная диагональ:", main_diag)
print("Сумма главной:", sum(main_diag))
print("Сумма побочной:", sum(side_diag))