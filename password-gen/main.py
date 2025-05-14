import string

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

