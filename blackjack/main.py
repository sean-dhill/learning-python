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
        while True:
            player_cards.append(playing_cards[random.randint(0, len(playing_cards) - 1)])
            print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
            print(f"Computer's first card: {computer_cards}")
            if sum(player_cards) > 21:
                print(f"Your final hand: {player_cards}, final score: {sum(player_cards)}")
                print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
                print("Game over, you went over 21!")
                game_on = False
                break
            new_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if new_card == 'n':
                break
    
    if sum(player_cards)<= 21:
        while sum(computer_cards) < 17:
            computer_cards.append(playing_cards[random.randint(0, len(playing_cards) - 1)])
        
        if sum(computer_cards) > 21:
            print(f"Your final hand: {player_cards}, final score: {sum(player_cards)}")
            print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
            print("Opponent went over. You win!")
            continue_game = input("Do you want to play a game of BlackJack? Type 'y' or 'n' ")
        
        if sum(player_cards) < sum(computer_cards):
            print(f"Your final hand: {player_cards}, final score: {sum(player_cards)}")
            print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
            print("Opponent won!")
            continue_game = input("Do you want to play a game of BlackJack? Type 'y' or 'n' ")
        
        if sum(player_cards) > sum(computer_cards):
            print(f"Your final hand: {player_cards}, final score: {sum(player_cards)}")
            print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
            print("You won!")
            continue_game = input("Do you want to play a game of BlackJack? Type 'y' or 'n' ")



