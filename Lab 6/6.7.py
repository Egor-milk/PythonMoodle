import random
n = int(input("N: "))
arr = [random.randint(1, 100) for _ in range(n)]
print("Массив:", *arr)

min_idx = arr.index(min(arr))
max_idx = arr.index(max(arr))
arr[min_idx], arr[max_idx] = arr[max_idx], arr[min_idx]

print("После замены min/max:", *arr)
print("Min был:", arr[max_idx])
print("Max был:", arr[min_idx])