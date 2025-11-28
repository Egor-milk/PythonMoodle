vklad1, vklad2 = 100000, 200000
year = 0

print("Год | 1-й вклад (10%) | 2-й вклад (2%)")
print("-" * 40)

while vklad1 <= vklad2:
    year += 1
    vklad1 *= 1.10  # Увеличиваем на 10%
    vklad2 *= 1.02  # Увеличиваем на 2%
    print(f"{year:^4} | {int(vklad1):^14} | {int(vklad2):^13}")

print(f"\nНа {year}-м году первый вклад превысил второй!")
print(f"1-й вклад: {int(vklad1)} руб.")
print(f"2-й вклад: {int(vklad2)} руб.")
