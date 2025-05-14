import string
import random

lowercase_letters = list(string.ascii_lowercase)
uppercase_letters = list(string.ascii_uppercase)
letters = lowercase_letters + uppercase_letters

digits = list(string.digits)

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
           '-', '_', '=', '+', '[', ']', '{', '}', '|', ';',
           ':', ',', '.', '<', '>', '?', '/']

print("Welcome to the Password Generator!")

number_letters = int(input("How many letters would you like in your password?: "))

number_digits = int(input("How many digits would you like in your password?: "))

number_symbols = int(input("How many symbols would you like in your password?: "))

random_letters = []
for letter in range(0, number_letters):
    random_index = random.randint(0,51)
    random_letters.append(letters[random_index])


random_digits = []
for digit in range(0, number_digits):
    random_index = random.randint(0,9)
    random_digits.append(digits[random_index])


random_symbols = []
for symbol in range(0,number_symbols):
    random_index = random.randint(0, len(symbols) - 1)
    random_symbols.append(symbols[random_index])


password_characters = random_letters + random_digits + random_symbols

random.shuffle(password_characters)

final_password = ''.join(password_characters)

print(f"Your final password with {number_letters} letters, {number_digits} digits and {number_symbols} symbols is: ", final_password)







