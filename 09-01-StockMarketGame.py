import random
import os
import json
import time

# === Financial Variables ===

stocks = [
    {
        "name": "SouthEastern Individual",
        "desc": "Life insurance company (Low Risk)",
        "sym": "SEI",
        "price": 50,
        "stock_left": random.randint(1, 100000)
    },
    {
        "name": "Orange",
        "desc": "Creator of the JPhone (High Risk)",
        "sym": "ORG",
        "price": 50,
        "stock_left": random.randint(1, 100000)
    },
    {
        "name": "Big Brother",
        "desc": "Owns Oodle and Distapound (Medium Risk)",
        "sym": "BB",
        "price": 50,
        "stock_left": random.randint(1, 100000)
    }
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

# === Other Variables ===

adTexts = ["Buy Crest Toothpaste today for only $9.99. 9.5 out of 10 doctors recommend it.", 
           "Buy Lay's potato chips now for $4.99. They are tasty!", 
           "Buy Jay's potato chips now for $4.99. They are tasty!",
           "Buy May's potato chips now for $4.99. They are tasty!", 
           "Buy potato chips now for $4.99. They are tasty!", 
           "Buy Red Baron frozen pizza now for $7.99. It is tasty!", 
           "Buy Jack's frozen pizza now for $7.99. It is tasty!", 
           "Buy Tombstone frozen pizza now for $7.98. It is tasty!", 
           "Buy DiGiorno frozen pizza now for $7.98. It is tasty!", 
           "Buy Stocks Premium now for $7.97. It is superior!"]

advertChance = int(random.random() * 100)
advertWait = 5

MarketCrashChance = int(random.random()*100)

# Show today's stock prices and the stocks you own
def DailyReport():
    print("\n=== DAY", Current_Day, "STOCK PRICES ===")
    for i, stock in enumerate(stocks):
        owned = User_Stocks.count(stock['sym'])
        total_supply = stock['stock_left'] + owned
        ownership_percent = (owned / total_supply) * 100 if total_supply > 0 else 0
        print(f"{i+1}. {stock['name']} ({stock['sym']}) : ${stock['price']} - {stock['desc']}")
    print()
    print("Your net worth is $", round(CalculateNetWorth(), 2))
    print(f"Your current cash balance: ${CurrentBalance:.2f}")

def OwnershipReport():
    print("\n=== OWNERSHIP REPORT ===")
    for stock in stocks:
        owned = User_Stocks.count(stock['sym'])
        total = owned + stock['stock_left']
        percent = (owned / total) * 100 if total > 0 else 0
        print(f"You own {percent:.2f}% of {stock['sym']}")
    print(f"Current Balance: ${CurrentBalance:.2f}")

def BuyStock():
    global CurrentBalance, AskedForCard

    if not AskedForCard:
        CreditPrompt()
        AskedForCard = True

    print("\n=== BUY STOCK ===")
    for i, stock in enumerate(stocks):
        print(f"{i+1}. {stock['name']} ({stock['sym']}) - ${stock['price']} (Available: {stock['stock_left']})")

    choice = int(input("Enter stock number: ")) - 1
    if 0 <= choice < len(stocks):
        stock = stocks[choice]
        print(f"Available shares of {stock['sym']}: {stock['stock_left']}")
        amount = int(input("How many shares to buy? "))

        if amount > stock["stock_left"]:
            print("Not enough shares available.")
            return

        total_cost = stock['price'] * amount
        if CurrentBalance >= total_cost:
            for _ in range(amount):
                User_Stocks.append(stock['sym'])
            stock["stock_left"] -= amount
            CurrentBalance -= total_cost
            print(f"Bought {amount} share(s) of {stock['sym']}.")
            CurrentBalance = round(CurrentBalance, 2)
            print("Current Balance", CurrentBalance)
        else:
            print("Not enough money.")
    else:
        print("Invalid choice.")

def SellStock():
    global CurrentBalance, AskedForCard

    if not AskedForCard:
        CreditPrompt()
        AskedForCard = True

    print("\n=== SELL STOCK ===")
    if not User_Stocks:
        print("You don't own any stocks.")
        return

    symbols = list(set(User_Stocks))
    for i, sym in enumerate(symbols):
        count = User_Stocks.count(sym)
        print(f"{i+1}. {sym} - {count} share(s)")

    choice = int(input("Enter stock number to sell: ")) - 1
    if 0 <= choice < len(symbols):
        sym = symbols[choice]
        amount = int(input("How many shares to sell? "))
        if User_Stocks.count(sym) >= amount:
            for _ in range(amount):
                User_Stocks.remove(sym)
            price = next(stock['price'] for stock in stocks if stock['sym'] == sym)
            stock = next(stock for stock in stocks if stock['sym'] == sym)
            stock["stock_left"] += amount  # Return shares to the market
            CurrentBalance += price * amount
            print(f"Sold {amount} share(s) of {sym}.")
            CurrentBalance = round(CurrentBalance, 2)
            print("Current Balance", CurrentBalance)
        else:
            print("You don't have that many shares.")
    else:
        print("Invalid choice.")

def ChangePrices():
    for i in stocks:
        if "High Risk" in i["desc"]:
            multiplier = random.uniform(0.0, 4.0)
        elif "Low Risk" in i["desc"]:
            multiplier = random.uniform(0.9, 1.2)
        else:
            multiplier = random.uniform(0.0, 3.0)

        i["price"] *= multiplier
        i["price"] = round(i["price"], 2)

def CalculateNetWorth():
    total_stock_value = 0
    for sym in set(User_Stocks):
        price = next(stock['price'] for stock in stocks if stock['sym'] == sym)
        total_stock_value += price * User_Stocks.count(sym)
    return CurrentBalance + total_stock_value

def CreditPrompt():
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

def Give_Prize():
    Bronze = ["candy bar", "funny sticker sheet", "certificate", "fidget toy"]
    Silver = ["5 dollar gift card", "notebook", "keychain", "snack pack"]
    Gold = ["mini succulent", "T-shirt", "portable phone stand", "10 dollar gift card"]
    Diamond = ["15 dollar gift card", "bluetooth speaker", "water bottle", "brain teaser game"]
    Platinum = ["20 dollar gift card", "wireless earbuds", "mini trophy", "desk lamp"]

    Net_Worth = CalculateNetWorth()
    if Net_Worth <= 1000:
        print("Congrats. Your rank is Bronze. You Won: " + random.choice(Bronze))
    elif Net_Worth > 1000 and Net_Worth <= 2500:
        print("Congrats. Your rank is Silver. You Won: " + random.choice(Silver))
    elif Net_Worth > 2500 and Net_Worth <= 5000:
        print("Congrats. Your rank is Gold. You Won: " + random.choice(Gold))
    elif Net_Worth > 5000 and Net_Worth <= 10000:
        print("Congrats. Your rank is Diamond. You Won: " + random.choice(Diamond))
    elif Net_Worth > 10000:
        print("Congrats. Your rank is Platinum. You Won: " + random.choice(Platinum))

def PrintCash():
    print(f"Current Cash Balance: ${CurrentBalance:.2f}")

def insertAd():
    chooseAd = int(random.random() * 10)
    if advertChance >= 10:
        print("===============================")
        print()
        print(adTexts[chooseAd])
        print()
        print("===============================")
        time.sleep(advertWait)
    else:
        print(" Want a break from the ads? Go ad free today for only $7.97.")
        time.sleep(advertWait)

#####################
# Main Gameplay Loop
#####################

while User_Choice != "Quit" and Current_Day <= Max_Day:
    DailyReport()
    print("\n=== MENU ===")
    print("Options: Buy / Sell / Account / End Day / Forget Card / Ownership Report / Quit")
    User_Choice = input("What would you like to do? ")

    if User_Choice == "Buy":
        BuyStock()
        PrintCash()
    elif User_Choice == "Sell":
        SellStock()
        PrintCash()
    elif User_Choice == "Account":
        print(f"Balance: ${CurrentBalance:.2f}")
        print(f"Stocks: {User_Stocks}")
        PrintCash()
    elif User_Choice == "Forget Card":
        if os.path.exists(CARD_FILE):
            os.remove(CARD_FILE)
            AskedForCard = False
            print("Your card info has been deleted.")
        else:
            print("No card info found.")
            PrintCash()
    elif User_Choice == "Ownership Report":
        OwnershipReport()
    elif User_Choice == "End Day":
        ChangePrices()
        insertAd()
        OwnershipReport()
        Current_Day += 1
    elif User_Choice == "Quit":
        break
    else:
        print("Invalid option.")

if MarketCrashChance >= 90:
    CurrentBalance = 0
    print("The stock market has crashed, sorry")

print(f"\nYour final cash balance is ${CurrentBalance:.2f}")
Give_Prize()
print("Goodbye!")
