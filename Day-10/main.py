# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price

# TODO-3: whether if new bids need to be added

bids = {}
print("Welcome to the secret auction program.")
should_continue = input("Are there any other bidders? Type 'yes' or 'no': \n ").lower()

continue_bidding = True
while continue_bidding:
    name = input ("What is your name?:")
    price = int(input("what is your bid?: "))       
    bids[name] = price 
    should_continue = input("Are there any other bidders? Type 'yes' or 'no': \n ").lower()

# TODO-4: Compare the bids and find the highest bid

