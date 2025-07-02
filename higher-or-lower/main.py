from data import game_data
from art import logo, vs
import random

game_over = False

personA = game_data[random.randint(0, len(game_data) - 1)]
personB = game_data[random.randint(0, len(game_data) - 1)]



print(f"Compare A: {personA['name']}, a {personA['description']}, from {personA['country']}")

print(f"Against B: {personB['name']}, a {personB['description']}, from {personB['country']}")

choice = input("Who has more followers? Type 'A' or 'B'").lower()

if personA['follower_count'] < personB['follower_count']:
    winner = 'b'
else:
    winner = 'a'

if choice == winner:
    print(f"You won person{winner.upper()} has more followers")
else:
    print("You lose")

