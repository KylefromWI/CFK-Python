import random
import os
import json

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


# Show today's stock prices and the stocks you own
def DailyReport():
    print("\n=== TODAY'S STOCK PRICES ===")
    for i, stock in enumerate(stocks):
        owned = User_Stocks.count(stock['sym'])
        total_supply = stock['stock_left'] + owned
        ownership_percent = (owned / total_supply) * 100 if total_supply > 0 else 0
        print(f"{i+1}. {stock['name']} ({stock['sym']}) : ${stock['price']} - {stock['desc']}")
        print(f"   Shares left: {stock['stock_left']}, You own: {owned} ({ownership_percent:.2f}%)")
    print()
    print("Your net worth is $", round(CalculateNetWorth(), 2))
    print("Today is Day", Current_Day)


# Buy stocks
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

    symbols = list(set(User_Stocks))
    for i, sym in enumerate(symbols):
        count = User_Stocks.count(sym)
        print(f"{i+1}. {sym} - {count} share(s)")
    if User_Choice == "Buy":
        BuyStock()
        print(f"Current Balance: ${CurrentBalance:.2f}")
    elif User_Choice == "Sell":
        SellStock()
        print(f"Current Balance: ${CurrentBalance:.2f}")
    elif User_Choice == "Account":
        print(f"Balance: ${CurrentBalance:.2f}")
        print(f"Stocks:")
        print(f"{i+1}. {sym} - {count} share(s)")
        print(f"Current Balance: ${CurrentBalance:.2f}")
    elif User_Choice == "Forget Card":
        if os.path.exists(CARD_FILE):
            os.remove(CARD_FILE)
            AskedForCard = False
            print("Your card info has been deleted.")
        else:
            print("No card info found.")
        print(f"Current Balance: ${CurrentBalance:.2f}")
    elif User_Choice == "End Day":
        ChangePrices()
        insertAd()
        print("\n=== OWNERSHIP REPORT ===")
        for stock in stocks:
            owned = User_Stocks.count(stock['sym'])
            total = owned + stock['stock_left']
            percent = (owned / total) * 100 if total > 0 else 0
            print(f"You own {percent:.2f}% of {stock['sym']}")
        Current_Day += 1
        print(f"Current Balance: ${CurrentBalance:.2f}")
    elif User_Choice == "Quit":
        break
    else:
        print("Invalid option.")
        print(f"Current Balance: ${CurrentBalance:.2f}")

print(f"\nYour final cash balance is ${CurrentBalance:.2f}")
Give_Prize()
print("Goodbye!")
