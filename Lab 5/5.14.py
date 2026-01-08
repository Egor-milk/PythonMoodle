str1 = input("Введите первую строку: ")
str2 = input("Введите вторую строку: ")

if str1 == str2:
    print("Строки одинаковые!")
else:
    print("Строки разные!")

    # разница в длине
    if len(str1) != len(str2):
        if len(str1) > len(str2):
            print(f"Первая строка длиннее на {len(str1) - len(str2)} символов")
        else:
            print(f"Вторая строка длиннее на {len(str2) - len(str1)} символов")

    found_difference = False
    position = 0

    # первое различие в символах
    min_length = min(len(str1), len(str2))
    while position < min_length:
        if str1[position] != str2[position]:
            print(f"Первое различие на позиции {position}: '{str1[position]}' vs '{str2[position]}'")
            found_difference = True
            break
        position += 1

