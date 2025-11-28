print("Введите стоимость реализованной продукции (руб.): ")
sales_amount = float(input())
print("Введите стаж работы в фирме (лет): ")
work_experience = int(input())

# Вычисление базовых комиссионных
if sales_amount >= 1000000:
    commission = sales_amount * 0.02  # 2%
else:
    commission = sales_amount * 0.01  # 1%

# Доплата за стаж
if work_experience >= 5:
    bonus = sales_amount * 0.005  # 0.5%
else:
    bonus = 0

# Общая сумма комиссионных
total_commission = commission + bonus
print(f"Стоимость реализованной продукции: {sales_amount:.2f} руб.")
print(f"Стаж работы: {work_experience} лет")
print(f"Базовые комиссионные ({commission/sales_amount*100:.1f}%): {commission:.2f} руб.")

if work_experience >= 5:
    print(f"Доплата за стаж (0.5%): {bonus:.2f} руб.")

print(f"Итого комиссионных: {total_commission:.2f} руб.")
