filename = "user_data.txt"
f = open(filename, "r", encoding='cp1251')
name = f.readline().strip()
surname = f.readline().strip()
email = f.readline().strip()
phone = f.readline().strip()


print(f"{name} {surname} – это вы. Ваша почта {email}, ваш телефон {phone}")