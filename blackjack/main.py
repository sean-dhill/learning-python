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

print(logo)

player_cards = [playing_cards[random.randint(0, len(playing_cards) - 1)],playing_cards[random.randint(0, len(playing_cards) - 1)]]
print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
    
computer_cards = [playing_cards[random.randint(0, len(playing_cards) - 1)]]
print(f"Computer's first card: {computer_cards}")
     
    
