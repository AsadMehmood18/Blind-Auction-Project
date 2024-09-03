from art import logo
print(logo)
data = {}
while True:
    # TODO-1: Ask the user for input
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    # TODO-2: Save data into dictionary {name: price}
    data[name] = bid
    highest_bid = 0
    winner = ""
    # TODO-4: Compare bids in dictionary
    for keys in data:
        if highest_bid < data[keys]:
            highest_bid = data[keys]
            winner = keys
    # TODO-3: Whether if new bids need to be added
    another = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if another =="no":
        print(f"The winner is {winner} with a bid of ${highest_bid}")
        break
    else:
        print("\n"*20)






