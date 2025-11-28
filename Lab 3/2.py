print("Введите количество грибов: ")
k = int(input())
if k % 10 == 1 and k % 100 != 11:
    word = "гриб"
elif 2 <= k % 10 <= 4 and (k % 100 < 10 or k % 100 >= 20):
    word = "гриба"
else:
    word = "грибов"

print(f"Мы нашли {k} {word} в лесу")
