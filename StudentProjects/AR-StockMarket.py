stocks = [
    {"name": "SouthEastern Individual", "desc": "Life insurance company", "sym": "SEI", "price": 50},
    {"name": "Orange", "desc": "Creator of the JPhone", "sym": "ORG", "price": 50},
    {"name": "Big Brother", "desc": "Owns Oodle and Distapound", "sym": "BB", "price": 50}
]

# Setup
print("Welcome User")
User_Name = input("What is your User_Name? ")
CurrentBalance = float(input("How much money would you like in your account? "))
User_Stocks = []

# Show stocks
def DailyReport():
    print("\n=== STOCK LIST ===")
    for i, stock in enumerate(stocks):
        print(f"{i+1}. {stock['name']} ({stock['sym']}) - ${stock['price']} - {stock['desc']}")
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

# Menu
print("\n=== MENU ===")
print("Options: Daily Report / Buy / Sell / Account / Exit")
User_Choice = input("What would you like to do? ")

while User_Choice != "Exit":
    if User_Choice == "Daily Report":
        DailyReport()
    elif User_Choice == "Buy":
        BuyStock()
    elif User_Choice == "Sell":
        SellStock()
    elif User_Choice == "Account":
        print(f"\nUser: {User_Name}")
        print(f"Balance: ${CurrentBalance}")
        print(f"Stocks: {User_Stocks}")
    else:
        print("Invalid option.")
    
    print("\nWhat would you like to do next?")
    User_Choice = input("Type: Daily Report / Buy / Sell / Account / Exit: ")

print("Goodbye!")

