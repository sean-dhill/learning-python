from data import game_data
from art import logo, vs
import random

game_over = False

personA = game_data[random.randint(0, len(game_data) - 1)]
personB = game_data[random.randint(0, len(game_data) - 1)]

score = 0
while game_over != True:
    print(logo)
    if score > 0:
        print(f"You're right! Current score {score}")
    
    print(f"Compare A: {personA['name']}, a {personA['description']}, from {personA['country']}")
    print(vs)
    print(f"Against B: {personB['name']}, a {personB['description']}, from {personB['country']}")

    choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    while choice not in ('a', 'b'):
        choice = input("Please enter 'A' or 'B': ")

    if personA['follower_count'] < personB['follower_count']:
        winner = 'b'
        winning_person = personB
    else:
        winner = 'a'
        winning_person = personA

    if choice == winner:
        score += 1
        personA = winning_person
        personB = game_data[random.randint(0, len(game_data) - 1)]
    else:
        print("You lose")
        game_over = True

