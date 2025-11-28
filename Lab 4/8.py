import random

counter = 0
for _ in range(15):
    if random.randint(0, 100) == 0:
        counter += 1

print(f'Количество чисел "0" в 15 сгенерированных случайных числах: {counter}')