import os
import platform

logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
ascii_logos = [
    r"""
    🏆
    """,
    r"""
    🎨
    """,
    r"""
    🎸
    """,
    r"""
    🍷
    """,
    r"""
    📦
    """,
    r"""
    👜
    """,
    r"""
    🎁
    """,
    r"""
    🛋️
    """,
    r"""
    🎟️
    """,
    r"""
    ⏰
    """
]


print(logo)


for logo in ascii_logos:
    print(f"Welcome to the auction! The item up for bid is: {logo}")
    auction_members = {}    
    continue_auction = True
    while continue_auction:
        name = input("Please enter name of bidding party: ")
        bid_amount = int(input("Please enter the amount you would like to bid: "))
        auction_members[name] = bid_amount 
        more_bidding_parties = input("Are there any more bidding parties? ").lower()
        
        while more_bidding_parties != 'yes' and more_bidding_parties != 'no':
            more_bidding_parties = input("Please enter either 'yes' or 'no' ")
        print("\n" * 25)

        if more_bidding_parties == 'no':
            highest_bid = 0
            for bidder in auction_members:
                if auction_members[bidder] > highest_bid:
                    highest_bidder = bidder
                    highest_bid = auction_members[bidder]
            print(f"{highest_bidder} has won the auction with a bid amount of {highest_bid}!")
            continue_auction = False

print("All auctions complete! Thank you for participating!")

    
