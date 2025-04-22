# Importing the logo from art.py
from art import logo
print(logo)

# This program is a simple auction system where users can place bids and the highest bidder wins.
# The program uses a dictionary to store the names and bids of the participants.
# The program will ask for the name and bid amount of each participant and store them in a dictionary.
# The program will then ask if there are any other bidders. If the answer is 'no', the program will find the highest bidder and print the result.
# The program will continue to ask for bids until the user indicates that there are no more bidders.

# Define a function to find the highest bidder
def find_highest_bidder(bidding_record):
    # Create a variable to keep track of the highest bid and the winner
    highest_bid = 0
    winner = ""
    # Iterate through the bidding record to find the highest bid
    for key in bidding_record:
        # Convert the bid amount to an integer
        bid_amount = int(bidding_record[key])
        # If the current bid is higher than the highest bid, update the highest bid and winner
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = key
    # Print the winner and the highest bid
    print(f"The winner is {winner} with a bid of ${highest_bid}")

# Initialize an empty dictionary to store the names and bids of the participants
people_bid = {}
is_over = False

# Inputs for the first time opening the program
# Print a welcome message
print("Welcome to the secret auction program.")
# Ask for the name and bid amount of the first participant
name = input("What is your name?:")
bid = input("What is your bid?: $")
people_bid[name] = bid
are_there_any = input("Are there any other bidders? Type 'yes or 'no'.").lower()

# Auction loop
while not  is_over:

    # If there are no more bidders, find the highest bidder and exit the loop
    if are_there_any == "no":
        # Stop the loop
        is_over = True
        # Call the function to find the highest bidder
        find_highest_bidder(people_bid)
    # If there are more bidders, ask for the name and bid amount of the next participant
    # and also user gives a wrong input, make sure to do not break the program
    else:
        # Clear the screen
        print("\n" * 100)
        # Print the logo again
        print(logo)
        # Ask for the name and bid amount of the next participant
        name = input("What is your name?:")
        bid = input("What is your bid?: $")
        people_bid[name] = bid
        are_there_any = input("Are there any other bidders? Type 'yes or 'no'.").lower()


# I know there is a better way to do this, but I am a beginner and I am trying to learn.
# I will try to improve my code in the future.
# I hope you like it.
# I am open to any suggestions or improvements.
# Thank you for your time.