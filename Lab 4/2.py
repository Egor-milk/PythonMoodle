population = 650000
year = 2013

print(f"Год: {year}, Население: {population}")

year = 2014
while year <= 2040:
    population = population * 1.03
    print(f"Год: {year}, Население: {int(population)}")
    year += 1
