email = input()

if '@' not in email or '.' not in email:
    print("Некорректный")
else:
    parts = email.split('@')
    if len(parts) != 2 or not parts[0] or not parts[1]:
        print("Некорректный")
    else:
        domain_parts = parts[1].split('.')
        if len(domain_parts) < 2 or len(domain_parts[-1]) < 2:
            print("Некорректный")
        else:
            print("Корректный")