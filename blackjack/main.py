import random


logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


playing_cards = [11,2,3,4,5,6,7,8,9,10,10,10]
game_on = True

while game_on:
    print(logo)
    
    player_cards = [random.choice(playing_cards), random.choice(playing_cards)]
    computer_cards = [random.choice(playing_cards)]
    
    print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
    print(f"Computer's first card: {computer_cards}")
    
    new_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    while new_card not in ('y','n'):
        new_card = input("Please enter either 'y' or 'n': ").lower()
    
    while new_card == 'y':
        player_cards.append(random.choice(playing_cards))
        print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
        print(f"Computer's first card: {computer_cards}")
        if sum(player_cards) > 21:
            break
        new_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    
    # Computer's turn
    while sum(computer_cards) < 17:
        computer_cards.append(random.choice(playing_cards))
    
    print(f"Your final hand: {player_cards}, final score: {sum(player_cards)}")
    print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
    
    # Determine the result
    if sum(player_cards) > 21:
        print("You went over 21! You lose.")
    elif sum(computer_cards) > 21:
        print("Opponent went over. You win!")
    elif sum(player_cards) == sum(computer_cards):
        print("It's a draw!")
    elif sum(player_cards) > sum(computer_cards):
        print("You won!")
    else:
        print("Opponent won!")
    
    # Ask to play again
    continue_game = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ").lower()
    if continue_game != 'y':
        game_on = False
        print("Thanks for playing!")



