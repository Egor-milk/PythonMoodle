num = int(input("Введите число: "))
total = 0
temp = num

while temp > 0:
    digit = temp % 10
    total += digit
    temp //= 10

print(f"Сумма цифр числа {num} равна {total}")
