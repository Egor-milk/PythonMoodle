words = input().split()
maxi = len(set(max(words, key = lambda x: len(set(x)))))
answer = [i for i in words if len(set(i)) == maxi]
print(*answer)
