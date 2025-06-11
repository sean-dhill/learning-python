import random

logo = r"""
 ____  _____                       __                          ______                                              
|_   \|_   _|                     [  |                       .' ___  |                                             
  |   \ | |  __   _   _ .--..--.   | |.--.   .---.  _ .--.  / .'   \_| __   _   .---.  .--.   .--.  .---.  _ .--.  
  | |\ \| | [  | | | [ `.-. .-. |  | '/'`\ \/ /__\\[ `/'`\] | |   ____[  | | | / /__\\( (`\] ( (`\]/ /__\\[ `/'`\] 
 _| |_\   |_ | \_/ |, | | | | | |  |  \__/ || \__., | |     \ `.___]  || \_/ |,| \__., `'.'.  `'.'.| \__., | |     
|_____|\____|'.__.'_/[___||__||__][__;.__.'  '.__.'[___]     `._____.' '.__.'_/ '.__.'[\__) )[\__) )'.__.'[___]                                                                                                                                                                                                                                                     
"""

print(logo)
print("Welcome to the Number Guessing Game")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard: ").lower()
random_number = random.randint(0,100)
num_lives = 0
if difficulty == "hard":
    num_lives = 5
else:
    num_lives = 10
    
while num_lives:
    guess = 0
    user_guess = int(input("Make a guess: "))
    guess = user_guess
    if user_guess < random_number:
        print("Too low")
        num_lives -= 1
        print(f"You have {num_lives} attempts remaining to guess the number")
    if user_guess > random_number: 
        print("Too high")
        num_lives -= 1
        print(f"You have {num_lives} attempts remaining to guess the number")
    if user_guess == random_number:
        print(f"You got it! The answer was {user_guess}")
        break
    
print(f"Good try. You're out of lives!! The number was {random_number}.")
        

