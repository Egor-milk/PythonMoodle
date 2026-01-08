def encrypt(text, key):
    encrypted = ""
    for i, char in enumerate(text):
        shift = (key + i) % 26
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted += char
    return encrypted

def decrypt(text, key):
    decrypted = ""
    for i, char in enumerate(text):
        shift = (key + i) % 26
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            decrypted += chr((ord(char) - base - shift) % 26 + base)
        else:
            decrypted += char
    return decrypted

# Пример использования
text = "Hello World!"
key = 5

print(f"Исходный текст: {text}")
encrypted = encrypt(text, key)
print(f"Зашифрованный:  {encrypted}")
decrypted = decrypt(encrypted, key)
print(f"Расшифрованный: {decrypted}")