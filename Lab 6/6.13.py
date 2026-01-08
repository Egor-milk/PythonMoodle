import random
matrix = [[random.randint(0, 99) for _ in range(3)] for _ in range(3)]
print("Исходная:", matrix)

flat = [x for row in matrix for x in row]
min_val, max_val = min(flat), max(flat)

for i in range(3):
    for j in range(3):
        if matrix[i][j] == min_val:
            matrix[i][j] = max_val
        elif matrix[i][j] == max_val:
            matrix[i][j] = min_val

print("После замены:", matrix)
print("Сумма всех элементов:", sum(flat))