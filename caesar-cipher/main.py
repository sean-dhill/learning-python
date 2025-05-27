def encrypt(original_text, shift_amount):
    new_string = ''
    for char in original_text:
        if char in alphabet:
            index_in_alphabet = alphabet.index(char)
            shifted_index = (index_in_alphabet + shift_amount) % 26
            new_string += alphabet[shifted_index]
        else:
            new_string += char
    print(f"Here is your encrypted result: {new_string} ")

def decrypt(original_text, shift_amount):
    decrypted_string = ''
    for char in original_text:
        if char in alphabet:
            index_in_alphabet = alphabet.index(char)
            shifted_index = index_in_alphabet - shift % 26
            decrypted_string += alphabet[shifted_index]
        else:
            decrypted_string += char
        
    print(f"Here is your decrypted result: {decrypted_string} ")



alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
continue_loop = True
while continue_loop:
    
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    while direction != 'encode' and  direction != 'decode':
        direction = input("Please enter either 'encode' or 'decode'")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    if direction == 'encode':
        encrypt(text, shift)
    if direction == 'decode':
        decrypt(text, shift)
    
    end_loop = input("Type 'yes' if you want to go again. Otherwise type 'no': ").lower()
    if end_loop == 'end':
        continue_loop = False