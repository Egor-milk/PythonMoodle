print('Введите номер месяца (от 1 до 12):')

month_number = int(input())

months = {
    1: "январь",
    2: "февраль",
    3: "март",
    4: "апрель",
    5: "май",
    6: "июнь",
    7: "июль",
    8: "август",
    9: "сентябрь",
    10: "октябрь",
    11: "ноябрь",
    12: "декабрь"
}

if 1 <= month_number <= 12:
    month_name = months[month_number]
    print(f"{month_number} - {month_name}")
else:
    print("Ошибка: введите число от 1 до 12")
