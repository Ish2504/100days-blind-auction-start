from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
print("Welcome to the secret auction program.")

def bidders_list(name, bid):
  bidders[name] = bid

bidders = {}
name = input("What is your name?: ")
bid = int(input("What's your bid?: $"))
bidders_list(name, bid)

bidding_is_finished = False

while not bidding_is_finished:
  more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
  if more_bidders == 'yes':
    clear()
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bidders_list(name, bid)
  else:

    bidding_is_finished = True
print(bidders.values())