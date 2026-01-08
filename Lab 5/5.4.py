s = input("Введите строку: ")
n = int(input("Введите максимальную длину подстроки (n): "))

result = []
current = ""

for word in s.split():
    # Если текущая подстрока пустая, пробуем добавить слово
    if current == "":
        if len(word) <= n:
            current = word
        else:
            print(f"Ошибка: слово '{word}' длиннее n={n}")
            exit()
    # Если слово помещается в текущую подстроку
    elif len(current) + 1 + len(word) <= n:
        current += " " + word
    # Если не помещается — сохраняем текущую и начинаем новую
    else:
        result.append(current)
        current = word

# Добавляем последнюю подстроку
if current:
    result.append(current)

# Вывод результата
print("Полученные подстроки:")
for i, sub in enumerate(result, 1):
    print(f"{i}: {sub} (длина {len(sub)})")