print("Welcome to the tip calculator!")

total_bill = input("What was the total bill? $ ")

tip_percentage = "1." + input("How much of a tip would you like to give? 10, 12 or 15%? ")

bill_after_tip = float(total_bill) * float(tip_percentage)

people_to_split = int(input("How many people to split the bill? "))

personal_bill = round(bill_after_tip / people_to_split, 2)

print(f"Each person should pay: ${personal_bill}")

