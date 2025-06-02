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

    player_cards = [playing_cards[random.randint(0, len(playing_cards) - 1)],playing_cards[random.randint(0, len(playing_cards) - 1)]]
    print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
    
    computer_cards = [playing_cards[random.randint(0, len(playing_cards) - 1)]]
    print(f"Computer's first card: {computer_cards}")
     
    new_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    while new_card not in ('y','n'):
        new_card = input("Please enter either 'y' or 'n': ")
    
    if new_card == 'y':
        while new_card == 'y':
            player_cards.append(playing_cards[random.randint(0, len(playing_cards) - 1)])
            print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
            print(f"Computer's first card: {computer_cards}")
            if sum(player_cards) > 21:
                print("Game over, you went over 21!")
                game_on = False
                break
            new_card = input("Type 'y' to get another card, type 'n' to pass: ")

