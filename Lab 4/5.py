x = int(input("Введите цену 1 кг конфет (руб.): "))

print("Вес (кг) | Стоимость (руб.)")
print("-" * 25)

for kg in range(1, 11):
    cost = x * kg
    print(f"{kg:^9} | {cost:^15}")
