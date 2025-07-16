# Written in class. Use this as a jumping off point

import random
import os
import json

# === Financial Variables ===

stocks = [
    {"name": "SouthEastern Individual", "desc": "Life insurance company (Low Risk)", "sym": "SEI", "price": 50},
    {"name": "Orange", "desc": "Creator of the JPhone (High Risk)", "sym": "ORG", "price": 50},
    {"name": "Big Brother", "desc": "Owns Oodle and Distapound (Medium Risk)", "sym": "BB", "price": 50}
]
CurrentBalance = 1000.00
User_Stocks = []

# === Loops and Choices ===
Max_Day = 6
Current_Day = 1
User_Choice = ""

# === Credit Card System ===
CARD_FILE = "card.json"
AskedForCard = os.path.exists(CARD_FILE)  # Already provided info?


# Show today's stock prices and the stocks you own
def DailyReport():
    print("\n=== TODAY'S STOCK PRICES ===")
    for i, stock in enumerate(stocks):
        print(f"{i+1}. {stock['name']} ({stock['sym']}) : ${stock['price']} - {stock['desc']}")
    print()
    print("Your Stocks:", User_Stocks)
    print("Your net worth is ", CalculateNetWorth())
    print("Today is day ", Current_Day)


# Buy stocks
def BuyStock():
    global CurrentBalance, AskedForCard

    if not AskedForCard:
        CreditPrompt()
        AskedForCard = True
    
    print("\n=== BUY STOCK ===")
    for i, stock in enumerate(stocks):
        print(f"{i+1}. {stock['name']} ({stock['sym']}) - ${stock['price']}")
    choice = int(input("Enter stock number: ")) - 1
    amount = int(input("How many shares to buy? "))
    if 0 <= choice < len(stocks):
        stock = stocks[choice]
        total_cost = stock['price'] * amount
        if CurrentBalance >= total_cost:
            for _ in range(amount):
                User_Stocks.append(stock['sym'])
            CurrentBalance -= total_cost
            print(f"Bought {amount} share(s) of {stock['sym']}.")
            CurrentBalance = round(CurrentBalance, 2)
            print("Current Balance", CurrentBalance)
        else:
            print("Not enough money.")
    else:
        print("Invalid choice.")

# Sell stocks
def SellStock():
    global CurrentBalance, AskedForCard
    
    if not AskedForCard:
        CreditPrompt()
        AskedForCard = True
    
    print("\n=== SELL STOCK ===")
    if not User_Stocks:
        print("You don't own any stocks.")
        return

    # Show Owned Stocks
    symbols = list(set(User_Stocks))
    for i, sym in enumerate(symbols):
        count = User_Stocks.count(sym)
        print(f"{i+1}. {sym} - {count} share(s)")

    choice = int(input("Enter stock number to sell: ")) - 1
    amount = int(input("How many shares to sell? "))
    if 0 <= choice < len(symbols):
        sym = symbols[choice]
        if User_Stocks.count(sym) >= amount:
            for _ in range(amount):
                User_Stocks.remove(sym)
            price = next(stock['price'] for stock in stocks if stock['sym'] == sym)
            CurrentBalance += price * amount
            print(f"Sold {amount} share(s) of {sym}.")
            CurrentBalance = round(CurrentBalance, 2)
            print("Current Balance", CurrentBalance)
        else:
            print("You don't have that many shares.")
    else:
        print("Invalid choice.")
'''
# Change the stock prices
def ChangePrices():
    for i in stocks:

        # random multiplier between 0% and 300%
        # The math looks like...
        #  random.random               =>  0.0 thru 1.0
        #  random.random * 3           =>  0.0 thru 3.0
        multiplier = random.random() * 3

        #multiply the previous price by the multipler, then make that the new price
        i["price"] = i["price"] * multiplier

        #round that price to the nearest cent
        i["price"] = round(i["price"], 2)'''

def ChangePrices(): # Stock Risk added by AR
    for i in stocks:
        # Risk-based multiplier ranges
        if "High Risk" in i["desc"]:
            multiplier = random.uniform(0.0, 4.0)     # Up to 400% (very volatile)
        elif "Low Risk" in i["desc"]:
            multiplier = random.uniform(0.9, 1.2)     # Small, steady changes
        else:
            multiplier = random.uniform(0.0, 3.0)     # Default (Medium Risk)

        i["price"] *= multiplier
        i["price"] = round(i["price"], 2)

def CalculateNetWorth(): #Written jointly by AR and VK
    total_stock_value = 0
    for sym in set(User_Stocks):
        price = next(stock['price'] for stock in stocks if stock['sym'] == sym)
        total_stock_value += price * User_Stocks.count(sym)
    return (CurrentBalance + total_stock_value)

def CreditPrompt(): #Written by LW
    print("\n*** SECURITY CHECK ***")
    print("Before you can trade stocks, please enter FAKE credit card info.")
    card_number = input("Enter Credit Card Number: ")
    exp_date = input("Enter Expiration Date (MM/YY): ")
    cvv = input("Enter Security Code (CVV): ")

    with open(CARD_FILE, "w") as f:
        json.dump({
            "card_number": card_number,
            "exp_date": exp_date,
            "cvv": cvv
        }, f)

    print("\nThanks! Your financial info has been stored.\n")

def insertAd(): #Written by OK
    def doAdd():
        chooseAdd = int(random.random()*10)
        if chooseAdd == 1:
            print("Buy Crest Toothpaste today for only $9.99. 9.5 out of 10 doctors recommend it.")
        elif chooseAdd == 2:
            print("Buy Lay's potato chips now for $4.99. They are tasty!")
        elif chooseAdd == 3:
            print("Buy Jay's potato chips now for $4.99. They are tasty!")
        elif chooseAdd == 4:
            print("Buy May's potato chips now for $4.99. They are tasty!")
        elif chooseAdd == 5:
            print("Buy potato chips now for $4.99. They are tasty!")
        elif chooseAdd == 6:
            print("Buy Red Baron frozen pizza now for $7.99. It is tasty!")
        elif chooseAdd == 7:
            print("Buy Jack's frozen pizza now for $7.99. It is tasty!")
        elif chooseAdd == 8:
            print("Buy Tombstone frozen pizza now for $7.98. It is tasty!")
        elif chooseAdd == 9:
            print("Buy DiGiorno frozen pizza now for $7.98. It is tasty!")
        else:
            print("Buy Stocks Premium now for $7.97. It is superior!")
    addChance = int(random.random()*100)
    if addChance >= 10:
        doAdd()
    else: print(" Want a break from the ads? Go ad free today for only $7.97.")

#####################
# Main Gameplay Loop
#####################

while User_Choice != "Quit" and Current_Day <= Max_Day:
    DailyReport()
    print("\n=== MENU ===")
    print("Options: Buy / Sell / Account / End Day / Quit")
    User_Choice = input("What would you like to do? ")

    if User_Choice == "Buy":
        BuyStock()
    elif User_Choice == "Sell":
        SellStock()
    elif User_Choice == "Account":
        print(f"Balance: ${CurrentBalance}")
        print(f"Stocks: {User_Stocks}")
    elif User_Choice == "Forget Card":
        if os.path.exists(CARD_FILE):
            os.remove(CARD_FILE)
            AskedForCard = False
            print("Your card info has been deleted.")
        else:
            print("No card info found.")
    elif User_Choice == "End Day":
        ChangePrices()
        Current_Day += 1
    else:
        print("Invalid option.")

print(f"Your final cash balance is ${CurrentBalance}")
print("Goodbye!")
