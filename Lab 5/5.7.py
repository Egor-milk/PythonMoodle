s = input('Введите строку: ')

result = ''

for char in s:
    result += char
    if char == 'а':
        result += 'а'

print(result)