words = input().split()
palindromes = []

for w in words:
    # Проверяем, состоит ли слово только из цифр
    if w.isdigit():
        # Проверяем, является ли оно палиндромом
        if w == w[::-1]:
            palindromes.append(w)

# Выводим результат
if len(palindromes) == 0:
    print("Нет слов-палиндромов из цифр")
elif len(palindromes) == 1:
    print(palindromes[0])
else:
    print(palindromes[1])  # второе слово (индекс 1)