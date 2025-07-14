import random

# Sets for color determination
red_numbers = {1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36}
black_numbers = {2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35}

def get_bet_amount(balance):
    while True:
        try:
            amount = float(input("How much money would you like to bet? $"))
            if 0 < amount <= balance:
                return amount
            else:
                print(f"Invalid amount. Your current balance is ${balance:.2f}")
        except ValueError:
            print("Please enter a valid number.")

def spin_wheel():
    number = random.randint(0, 36)
    if number == 0:
        color = "Green"
    elif number in red_numbers:
        color = "Red"
    else:
        color = "Black"
    return number, color

def play_roulette():
    balance = float(input("Enter your starting money: $"))
    
    while balance > 0:
        print("\nBet Options:")
        print("1. Specific Number (1–36) – 35x payout")
        print("2. Color (Red or Black) – 2x payout")
        print("3. Thirds (1st 12, 2nd 12, 3rd 12) – 3x payout")
        print("4. Halves (1st 18 or 2nd 18) – 2x payout")
        print("5. Even or Odd – 2x payout")

        choice = input("What would you like to bet on? (1-5): ").strip()
        bet_amount = get_bet_amount(balance)

        won = False

        if choice == "1":
            bet = input("Enter a number between 1 and 36: ").strip()
            number, color = spin_wheel()
            print(f"\nRoulette spun... Result: {number} {color}")
            if bet.isdigit() and 1 <= int(bet) <= 36 and int(bet) == number:
                balance += bet_amount * 35
                print(f"You won! +${bet_amount * 35:.2f}")
                won = True

        elif choice == "2":
            bet = input("Choose a color (Red or Black): ").strip().capitalize()
            number, color = spin_wheel()
            print(f"\nRoulette spun... Result: {number} {color}")
            if bet == color:
                balance += bet_amount
                print(f"You won! +${bet_amount:.2f}")
                won = True

        elif choice == "3":
            bet = input("Choose '1st 12', '2nd 12', or '3rd 12': ").strip().lower()
            number, color = spin_wheel()
            print(f"\nRoulette spun... Result: {number} {color}")
            if ((bet == "1st 12" and 1 <= number <= 12) or
                (bet == "2nd 12" and 13 <= number <= 24) or
                (bet == "3rd 12" and 25 <= number <= 36)):
                balance += bet_amount * 2
                print(f"You won! +${bet_amount * 2:.2f}")
                won = True

        elif choice == "4":
            bet = input("Choose '1st 18' or '2nd 18': ").strip().lower()
            number, color = spin_wheel()
            print(f"\nRoulette spun... Result: {number} {color}")
            if ((bet == "1st 18" and 1 <= number <= 18) or
                (bet == "2nd 18" and 19 <= number <= 36)):
                balance += bet_amount
                print(f"You won! +${bet_amount:.2f}")
                won = True

        elif choice == "5":
            bet = input("Choose 'Even' or 'Odd': ").strip().capitalize()
            number, color = spin_wheel()
            print(f"\nRoulette spun... Result: {number} {color}")
            if (bet == "Even" and number != 0 and number % 2 == 0) or \
               (bet == "Odd" and number % 2 == 1):
                balance += bet_amount
                print(f"You won! +${bet_amount:.2f}")
                won = True

        if not won:
            balance -= bet_amount
            print(f"You lost. -${bet_amount:.2f}")

        print(f"Current Balance: ${balance:.2f}")

        if balance <= 0:
            print("You're out of money. Game over!")
            break

        play_again = input("Play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            break

    print(f"\nGame ended. Final balance: ${balance:.2f}. Thanks for playing!")

play_roulette()
RouletteGame.py
Displaying RouletteGame.py.
