import random

hangman_stages = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]

hangman_logo = """
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \\ / _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                    __/ |                     
                   |___/                      
"""

hangman_words = [
    "cat", "tree", "ship", "gold", "mask", "rope", "book", "wolf",
    "apple", "brain", "chair", "cloud", "snake", "robot", "lunar", "flame",
    "castle", "garden", "window", "school", "rocket", "planet", "pirate", "tunnel",
    "umbrella", "sandwich", "triangle", "elephant", "mountain", "dinosaur", "keyboard", "backpack",
    "adventure", "volcano", "telescope", "chocolate", "treasure", "invisible", "reptilian", "magnetism"
]



random_word = hangman_words[random.randint(0, len(hangman_words) - 1)]


hidden_word = ['_' for _ in random_word]
    


print(hangman_logo)
print(random_word)
game_over = False
life_count = 6
letters_left_to_guess = len(random_word)
incorrect_guesses = 0
 
while not game_over:
    
    print(f'Word to guesss : ')
    print(''.join(hidden_word))
    letter_guess = input("Guess a letter: ")

    index = 0
    correct_guess = False

    for letter in random_word:
        if letter == letter_guess:
            hidden_word[index] = letter_guess
            letters_left_to_guess -= 1
            correct_guess = True
        index += 1
    
    if correct_guess == False:
        incorrect_guesses += 1
        life_count -= 1
        print(f"You guessed {letter_guess}, thats not in the word. You lose a life.")
    
    if life_count == 0:
        print("You ran out of lives! Game over!")
        game_over = True
    
    if letters_left_to_guess == 0:
        print("You won! you guessed all the letters! Game Over!")
        game_over = True
    print(hangman_stages[incorrect_guesses])
    print(f"****************************** {life_count}/6 LIVES LEFT ******************************")
    








