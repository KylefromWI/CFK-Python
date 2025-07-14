#Code written by or at the direction of LW

import random
import json
import sys
import time

# Constants
MAX_DAYS = 6
SAVE_FILE = "game_save.json"

# Initial data
stocks = [
    {"name": "SouthEastern Individual", "desc": "Everyone's favorite life insurance company", "sym": "SEI", "price": 50},
    {"name": "Orange", "desc": "Creator of the JPhone", "sym": "ORG", "price": 50},
    {"name": "Big Brother", "desc": "Owner of companies like Oodle and distapound", "sym": "BB", "price": 50}
]

acct = {"cash": 1000, "SEI": 0, "ORG": 0, "BB": 0}
currentDay = 1

# Helper Functions
def handle_input(prompt):
    user_input = input(prompt).strip()
    if user_input == "Great Depression":
        def scroll(text, delay=1.5):
            print(text)
            time.sleep(delay)

        print("\n=== Historical Event in Progress: The Great Depression (1929–1939) ===\n")
        time.sleep(1.5)

        scroll("The stock market crashes in October 1929, sending shockwaves through the U.S. economy.")
        scroll("Investors panic, banks close, and businesses begin to fail at a rapid pace.")
        scroll("Unemployment rises sharply — one in four Americans loses their job.")
        scroll("Families struggle to survive as savings disappear and homes are lost.")
        scroll("Thousands of banks shut down, and credit becomes unavailable.")
        scroll("Consumer spending collapses.")

        scroll("The crisis spreads quickly to Europe and other parts of the world.")
        scroll("Global trade contracts. Economies enter deep, prolonged recessions.")

        scroll("In the U.S., the federal government begins emergency intervention.")
        scroll("President Franklin D. Roosevelt launches the New Deal.")
        scroll("Public works programs are created. Banks are regulated. Social support systems are introduced.")

        scroll("Despite these efforts, economic hardship continues for years.")
        scroll("It takes the global demands of World War II to fully restore industrial growth and employment.")

        scroll("\nThe game ends as the world experiences the worst financial collapse of the 20th century.")
        sys.exit("Game terminated due to historical catastrophe: The Great Depression.")
    return user_input

def save_game():
    game_state = {
        "stocks": stocks,
        "acct": acct,
        "currentDay": currentDay
    }
    with open(SAVE_FILE, "w") as f:
        json.dump(game_state, f, indent=2)
    print("Game saved.")

def load_game():
    global stocks, acct, currentDay
    try:
        with open(SAVE_FILE, "r") as f:
            data = json.load(f)
            stocks = data["stocks"]
            acct = data["acct"]
            currentDay = data["currentDay"]
            print("Game loaded.")
    except FileNotFoundError:
        print("No saved game found. Starting new game.")

def print_daily_report():
    print(f"\n=== Day {currentDay} ===")
    print(f"Cash: ${acct['cash']:.2f}")
    for stock in stocks:
        sym = stock["sym"]
        print(f"{stock['name']} ({sym}) - Price: ${stock['price']} - Shares: {acct[sym]}")

def user_choices():
    while True:
        choice = handle_input("What do you want to do? (buy, sell, end day, save, load): ").lower()
        if choice == "buy":
            buy_stocks()
            break
        elif choice == "sell":
            sell_stocks()
            break
        elif choice == "end day":
            end_day()
            break
        elif choice == "save":
            save_game()
        elif choice == "load":
            load_game()
        else:
            print("Invalid choice. Try again.")

def get_stock_by_input(user_input):
    for stock in stocks:
        if stock["name"].lower() == user_input.lower() or stock["sym"].lower() == user_input.lower():
            return stock
    return None

def buy_stocks():
    user_input = handle_input("Enter stock name or symbol to buy: ")
    stock = get_stock_by_input(user_input)
    if not stock:
        print("Invalid stock.")
        return

    try:
        shares = int(handle_input("How many shares to buy? "))
        cost = shares * stock["price"]
        if acct["cash"] >= cost:
            acct[stock["sym"]] += shares
            acct["cash"] -= cost
            print(f"Bought {shares} shares of {stock['name']}")
        else:
            print("Not enough cash.")
    except ValueError:
        print("Invalid number of shares.")

def sell_stocks():
    user_input = handle_input("Enter stock name or symbol to sell: ")
    stock = get_stock_by_input(user_input)
    if not stock:
        print("Invalid stock.")
        return

    try:
        shares = int(handle_input("How many shares to sell? "))
        if acct[stock["sym"]] >= shares:
            acct[stock["sym"]] -= shares
            acct["cash"] += shares * stock["price"]
            print(f"Sold {shares} shares of {stock['name']}")

            # 10% chance of crash
            if random.random() < 0.1:
                print("!!! MARKET CRASH !!!")
                for s in stocks:
                    s["price"] = max(1, s["price"] // 2)
        else:
            print("Not enough shares.")
    except ValueError:
        print("Invalid number of shares.")

def change_prices():
    for stock in stocks:
        change = random.randint(-10, 10)
        stock["price"] = max(1, stock["price"] + change)

def end_day():
    global currentDay
    print("Ending day...")
    change_prices()
    currentDay += 1

def final_results():
    print("\n=== Final Report ===")
    total = acct["cash"]
    print(f"Cash: ${acct['cash']:.2f}")
    for stock in stocks:
        sym = stock["sym"]
        shares = acct[sym]
        value = shares * stock["price"]
        print(f"{stock['name']} ({sym}): {shares} shares @ ${stock['price']} = ${value}")
        total += value
    print(f"Total Portfolio Value: ${total:.2f}")

# Main game loop
load_game()
while currentDay <= MAX_DAYS:
    print_daily_report()
    user_choices()

final_results()
Stonks.py
Displaying Stonks.py.
