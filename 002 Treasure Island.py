import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list = []
for p_letters in range(1, nr_letters + 1):
    x = letters[random.randint(0, 51)]
    password_list.append(x)

for p_symbols in range(1, nr_symbols + 1):
    x = symbols[random.randint(0, 8)]
    password_list.append(x)

for p_numbers in range(1, nr_numbers + 1):
    x = numbers[random.randint(0, 9)]
    password_list.append(x)


random.shuffle(password_list)
final_password = ""

for x in password_list:
    final_password += x

print(f"Your password is: {final_password}")
