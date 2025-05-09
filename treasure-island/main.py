print("Welcome to Treasure Island!\n")
print("Your mission is to find the treasure hidden at the end of the journey.\n")

choice1 = input("To begin your journey, do you go left or right? ")

if choice1 == "left" or  choice1 == "Left":
    choice2 = input("You are confronted by a river, do you choose to swim across the river or try to walk around it? ")
    print("\n")
    
    if choice2.lower() == "swim across" or choice2.lower() == "swim":
        print("You drowned, Game Over!")

    elif choice2.lower() == "walk" or choice2.lower() == "walk around" or choice2 == "walk around it":
        print("You walk around the river and encounter a bridge, over the bridge you find 3 doors;")
        choice3 = input("a Red door, a Blue Door and a Yellow door, which door do you enter? ")

        if choice3.lower() == "red":
            print("You fell into a pit of fire and died! Game Over!")
        elif choice3.lower() == "blue":
            print("You are eaten by beasts! Game Over!")
        elif choice3.lower() == "yellow":
            print("You found the Treasure! You Win!")
        else:
            print("You failed to pick a valid door and got eaten by the troll under the bridge!")
    

elif choice1 == "right" or "Right":
    print("You fall into a hole, Game Over!")