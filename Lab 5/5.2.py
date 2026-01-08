s = input().strip()
print("Исходная строка:", s)

words = s[:-1].split()
max_b_count = -1
word_to_remove = -1

for i, word in enumerate(words):
    b_count = word.count('В')
    if b_count > max_b_count:
        max_b_count = b_count
        word_to_remove = i

if max_b_count == 0:
    print("Слов с буквой 'В' нет")
else:
    words.pop(word_to_remove)
    result = ' '.join(words) + '.'
    print("Преобразованная строка:", result)