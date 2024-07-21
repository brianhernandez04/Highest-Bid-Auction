import os

def clear():
    os.system('cls')

clear()

print("Welcome to the secret bidding auction")

end_of_bid = False
bidding_data = []

while end_of_bid == False:

    user_name = input("What is your name? ").lower()
    user_bid = int(input("What is your bid? $"))
    alt_users = input("Are there any other bidders? Type either 'yes' or 'no': ").lower()

    def user_info(name, bid):
        user_data = {}
        user_data["Bidder"] = name
        user_data["Amount"] = bid
        bidding_data.append(user_data)
    if alt_users == "yes":
        user_info(user_name, user_bid) 
        clear()
        end_of_bid = False
    else:
        user_info(user_name, user_bid) 
        end_of_bid = True 

highest_bid = 0
highest_bidder = ""
amounts = [items ["Amount"] for items in bidding_data]
max_amount = max(amounts)


for items in bidding_data:
    if items["Amount"] == max_amount:
        highest_bid = items["Amount"]
        highest_bidder = items["Bidder"]

print(f"The heighest bid is ${highest_bid} and the highest bidder is {highest_bidder}")

