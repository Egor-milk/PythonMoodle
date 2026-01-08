cars = ["Toyota", "BMW", "Audi", "Ford", "Mercedes", "Honda"]

print("Исходный:", cars)

# По возрастанию
sorted_asc = sorted(cars)
print("По возрастанию:", sorted_asc)

# По убыванию
sorted_desc = sorted(cars, reverse=True)
print("По убыванию:", sorted_desc)

# Или сортировка на месте
cars.sort()
print("По возрастанию (на месте):", cars)
cars.sort(reverse=True)
print("По убыванию (на месте):", cars)