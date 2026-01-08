s = input()
letters = 'abcde'
counts = []

for letter in letters:
    cnt = s.count(letter)
    if cnt > 0:
        counts.append(f"{letter}: {cnt}")

if counts:
    print(*counts, sep='\n')
else:
    print("Нет")