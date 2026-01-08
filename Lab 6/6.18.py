import random

arr = [random.randint(0, 1000) for _ in range(20)]
print("До:", arr)

for i in range(len(arr)):
    for j in range(len(arr)-1-i):
        if arr[j] < arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print("После:", arr)