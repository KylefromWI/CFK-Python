import random

stocks = [
    {"name": "SouthEastern Individual", "desc": "Life insurance company", "sym": "SEI", "price": 50},
    {"name": "Orange", "desc": "Creator of the JPhone", "sym": "ORG", "price": 50},
    {"name": "Big Brother", "desc": "Owns Oodle and Distapound", "sym": "BB", "price": 50}
]
CurrentBalance = 1000.00
User_Stocks = []
Max_Day = 6
Current_Day = 1
User_Choice = ""

# Show today's stock prices and the stocks you own
def DailyReport():
    print("\n=== TODAY'S STOCK PRICES ===")
    for i, stock in enumerate(stocks):
        print(f"{i+1}. {stock['name']} ({stock['sym']}) : ${stock['price']} - {stock['desc']}")
    print()
    print("Your Stocks:", User_Stocks)

# Buy stocks
def BuyStock():
    global CurrentBalance
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
            print("Current Balance", CurrentBalance)
        else:
            print("Not enough money.")
    else:
        print("Invalid choice.")

# Sell stocks
def SellStock():
    global CurrentBalance
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
            print("Current Balance", CurrentBalance)
        else:
            print("You don't have that many shares.")
    else:
        print("Invalid choice.")

# Change the stock prices
def ChangePrices():
    for i in stocks:

        # random multiplier between -200% and 200%
        # The math looks like...
        #  random.random               =>  0.0 thru 1.0
        #  random.random - 0.5         => -0.5 thru 0.5
        # (random.random() - 0.5) * 4  => -2.0 thru 2.0   
        multiplier = (random.random() - 0.5) * 4

        #multiply the previous price by the multipler, then make that the new price
        i["price"] = i["price"] * multiplier

        #round that price to the nearest cent
        i["price"] = round(i["price"], 2)


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
    elif User_Choice == "End Day":
        ChangePrices()
        Current_Day += 1
    else:
        print("Invalid option.")

print(f"Your final cash balance is ${CurrentBalance}")
print("Goodbye!")
