#Supposed to be like BlackJack

import time
import random

Ace = [1,11]

deck = [2,3,4,5,6,7,8,9,10,10,10,10,10,11,1,2,3,4,5,6,7,8,9,10,10,10,10,10,11,1,2,3,4,5,6,7,8,9,10,10,10,10,10,2,3,4,5,6,7,8,9,10,10,10,10,10]

DealerHand = 0
PlayerHand = 0

wins = 0

select = ""

answer = input("Do you want to Play Blackjack?")

if answer == "yes":
    
    while PlayerHand <22:
        #Dealer's Hand
        print("Dealer's Hand:")
        card = int(random.choice(deck))
        DealerHand = DealerHand + card
        print(card)
        deck.remove(card)
        time.sleep(0.5)

        card = int(random.choice(deck))
        DealerHand = DealerHand + card
        print("X")
        deck.remove(card)
        time.sleep(0.5)
        
        #Your Cards
        print("Your Hand:")
        card = int(random.choice(deck))
        print(card)
        PlayerHand = PlayerHand + card
        deck.remove(card)
        time.sleep(0.5)
        
        card = int(random.choice(deck))
        print(card)
        PlayerHand = PlayerHand + card
        deck.remove(card)
        
        select = input("What do you want to do?   (hit/check)")    #check or hit
            
        while select == "hit":
            card = int(random.choice(deck))
            print(card)
            PlayerHand = PlayerHand + card
            deck.remove(card)
            time.sleep(2)
            select = input("What do you want to do?")
        else:
            print("Your Hand: ", PlayerHand)
            time.sleep(1)
        
        if PlayerHand > 21:
            print("You Busted!")
            wins = wins-1
            print("Score: ", wins)
            time.sleep(5)
            print("")
            print("Play Again!")    
            DealerHand = 0
            PlayerHand = 0
            continue
        
        select = input("Type fold if u want to fold? (Lose no score)") 
        
        if select == "fold":
            print("Folded! (Keep Score)")
            print("Current Score: ", wins)
            time.sleep(5)
            print("")
            print("Play Again!")
            DealerHand = 0
            PlayerHand = 0
            continue
            
        
        print("Dealer's Hand: ", DealerHand)
        time.sleep(2)
        
        while DealerHand < 17:
            print("Dealer Draws an Extra Card")
            time.sleep(2)
            card = int(random.choice(deck))
            print(card)
            time.sleep(2)
            DealerHand = DealerHand + card
            deck.remove(card)
        else:
            print("Dealer's Hand: ", DealerHand)
        time.sleep(2)
        
        if DealerHand > 21:
            print("Dealer Busted")
            time.sleep(1)
            print("You Win!")
            time.sleep(1)
            wins = wins+1
            print("Current Score: ", wins)
            time.sleep(5)
            print("")
            print("Play Again!")
            DealerHand = 0
            PlayerHand = 0
            
        
        if PlayerHand > DealerHand:
            print("You Win!")
            time.sleep(1)
            wins = wins+1
            print("Current Score: ", wins)
            time.sleep(5)
            print("")
            print("Play Again!")
            DealerHand = 0
            PlayerHand = 0
        elif DealerHand > PlayerHand:
            print("You Lose :(  (lose a Score)")
            time.sleep(1)
            wins = wins-1
            print("Current Score: ", wins)
            time.sleep(5)
            print("")
            print("Play Again!")
            DealerHand = 0
            PlayerHand = 0
        elif PlayerHand == DealerHand:
            print("Draw (Keep Score)")
            print("Current Score: ", wins)
            time.sleep(5)
            print("")
            print("Play Again!")
            DealerHand = 0
            PlayerHand = 0
        
        deck = [2,3,4,5,6,7,8,9,10,10,10,10,10,11,1,2,3,4,5,6,7,8,9,10,10,10,10,10,11,1,2,3,4,5,6,7,8,9,10,10,10,10,10,2,3,4,5,6,7,8,9,10,10,10,10,10]
        
    else:
        print("You Busted!")
        print("Score: ", wins)    
        
else:
    print("You Miss %100 of the Shots You Don't Take")
    print("Bad Dealear Cards Too Haha")
    time.sleep(2)
    print("Try Again")
