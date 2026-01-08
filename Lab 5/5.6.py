s = input()

mid = len(s) // 2

second = s[mid:]

revers_second = ''
for i in range(len(second)-1, -1, -1):
    revers_second += second[i]

print("Исходная строка",s)
print("Полученная строка",revers_second)
