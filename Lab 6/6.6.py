import random
n = int(input("N: "))
arr = [random.randint(1, 100) for _ in range(n)]
print("До:", *arr)
arr[0], arr[-1] = arr[-1], arr[0]
print("После:", *arr)