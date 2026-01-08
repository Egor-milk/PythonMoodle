import random
C = [[random.randint(0, 99) for _ in range(3)] for _ in range(3)]
D = [[random.randint(0, 99) for _ in range(3)] for _ in range(3)]

# Сложение
sum_matrix = [[C[i][j] + D[i][j] for j in range(3)] for i in range(3)]
# Умножение
mul_matrix = [[sum(C[i][k] * D[k][j] for k in range(3)) for j in range(3)] for i in range(3)]

print("C:", C)
print("D:", D)
print("Сумма:", sum_matrix)
print("Произведение:", mul_matrix)