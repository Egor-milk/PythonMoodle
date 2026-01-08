from collections import Counter


s = input().strip().split()
answer = []
for i, j in enumerate(s):
    if Counter(j)['А'] > 3:
        answer.append(i)
if len(answer) == 0:
    print('Таких слов нет')
else:
    print(answer)

