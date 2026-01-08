import random
n = int(input("N: "))
arr = [random.randint(1, 100) for _ in range(n)]
print(*arr)