num = input("Введите целое число: ")

palindrome = num == num[::-1]

if palindrome:
    print(f"{num} — является палиндромом.")
else:
    print(f"{num} —  не является палиндромом.")
