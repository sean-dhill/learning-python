import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
     _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
playing = True
player_score = 0
computer_score = 0

while playing:
    choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: ")

    computer_choice = random.randint(0, 2)

    

    if choice == "0":
        print(f"{rock}")
    elif choice == "1":
        print(f"{paper}")
    else:
        print(f"{scissors}")

    if computer_choice == 0:
        print("Computer chose:")
        print(f"{rock}")
    elif computer_choice == 1:
        print("Computer chose: ")
        print(f"{paper}")
    else:
        print("Computer chose: ")
        print(f"{scissors}")

    choice = int(choice)

    if choice == computer_choice:
        print("Its a draw")

    if choice == 0 and computer_choice == 1:
        print("Computer wins, Paper beats Rock!")
        computer_score += 1

    if choice == 0 and computer_choice == 2:
        print("You win, Rock beats Scissors!")
        player_score += 1

    if choice == 1 and computer_choice == 0:
        print("You win, Paper beats Rock!")
        player_score += 1

    if choice == 1 and computer_choice == 2:
        print("Computer wins, Scissor beats Paper!")
        computer_score += 1

    if choice == 2 and computer_choice == 0:
        print("Computer wins! Rock beats Scissors!")
        computer_score += 1

    if choice == 2 and computer_choice == 1:
        print("You win! Scissor beats Paper!")
        player_score += 1

    print("Current score:")
    print(f"Player: {player_score}    Computer: {computer_score}")
    
    keep_playing = input("Would you like to keep playing? Input 'Y' for yes and 'N' for no: ").lower()
    while keep_playing not in ["y", "n"]:
        keep_playing = input("Please enter 'Y' or 'N': ")