print("°C\t°F")
for celsius in range(15, 39):
    fahrenheit = 1.8 * celsius + 32
    print(f"{celsius}\t{fahrenheit:.1f}")
