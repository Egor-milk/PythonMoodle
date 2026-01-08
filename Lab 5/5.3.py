# Ввод количества строк
n = int(input())
A = [input() for _ in range(n)]

# Гласные буквы (русские и английские)
vowels = "АЕЁИОУЫЭЮЯAEIOU"
B = []

# Обработка каждой строки
for s in A:
    words = s.split()
    count = 0
    for w in words:
        if w and w[0].upper() in vowels:
            count += 1
    B.append(count)

# Вывод результата
print("Исходный массив:")
for s in A:
    print(s)

print("\nМассив B:")
print(*B)