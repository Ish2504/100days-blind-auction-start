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
    clear()
    max_bidder_value = max(bidders.values())
    for k,v in bidders.items():
      if v == max_bidder_value:
        print(f"The winner is {k} with a bid of ${v}")
    bidding_is_finished = True
