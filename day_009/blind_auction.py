import os
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\ 
                         `'-------'`
                       .-------------.
                      /_______________\ 
'''
print(logo)
bids = {}
more = "yes"
while more == "yes":
    print("Welcome to the silent auction program!")
    name = input("Please enter your name: ")
    bid = int(input("Please enter your bid amount: $"))
    bids[name] = bid
    more = input("Are there any more bidders? Type 'yes' or 'no': ").lower()
    os.system('clear')
bid = 0
bidder = ""
for key, value in bids.items():
    if value > bid:
        bid = value
        bidder = key
print(f"The winner is {bidder} with a bid amount of ${bid}\nCongratulations {bidder}!!!")
