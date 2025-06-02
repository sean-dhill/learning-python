logo = r"""
 _____________________
|  _________________  |
| |                0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply,
}

continue_loop = True

while True:
    print(logo)
    first_number = float(input("What is the first number?: "))
    
    while True:
        operation = input("+\n-\n/ \n*\nWhat operation would you like to perform?: ")
        while operation not in ("+","-","/","*"):
            operation = input("+\n-\n/ \n*\nPlease enter a valid operation: ")
        
        second_number = float(input("What is the next number?: "))
        result = operations[operation](first_number,second_number)

        print(f"{first_number} {operation} {second_number} = {operations[operation](first_number,second_number)}")
        continue_loop = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
        while continue_loop not in ("n","y"):
            continue_loop = input("Please enter 'y' or 'n': ")
        if continue_loop == "y":
            first_number = result
        else:
            break
    