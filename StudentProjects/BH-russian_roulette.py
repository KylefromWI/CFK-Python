#Code written by BH

import random
import time
file_object = open("scores.txt")
streak = 0
alive = True
hiScore = file_object.read()
hiScore = int(hiScore)
print(hiScore)
gameover = False
trigger = 0
blanknum = 5
bulletnum = 1
print("Russian roulette")
input(" press ENTER to play")


def plurals(number):
    if number - 1> 1:
        return "s"
    else:
        return ""

def smallnum(x, y):
    return random.randint(x, y)/10

def load():
    currentNumber = 1
    blanknum = 5
    print("you load")
    time.sleep(.3)
    while int(currentNumber) <= blanknum:
        print(currentNumber)
        time.sleep(smallnum(2, 6))
        currentNumber += 1
    print("blank",plurals(currentNumber), " and", sep='')
    currentNumber = 1
    while currentNumber <= bulletnum:
        print(currentNumber)
        time.sleep(smallnum(2, 6))
        currentNumber += 1
    time.sleep(1)
    print("round", plurals(currentNumber), sep='')
    time.sleep(1)

load()

while alive == True and gameover == False:
    totalnum = blanknum + bulletnum
    print("you spin the chamber")
    time.sleep(1.8)
    match input("the gun is aimed. press F to fire, press L to lower the gun"):
        case "F" | "f":
            time.sleep(0.1)
            trigger = random.randint(bulletnum,totalnum)
            if trigger == 1:
                print("BANG!")
                time.sleep(1.5)
                print("you died")
                alive = False
            elif trigger != 1 and trigger != 0:
                streak += 1
                print("-click-")
                blanknum -= 1
                print("there are",blanknum, "blanks")
                if blanknum == 0:
                    print("all chambers have been fired")
                    match input("would you like to keep going? Y for yes, N for no"):
                        case "Y" | "y":
                            load()
        case "wipe":
            hiScore = 0
            print("the data has been wiped")
        case _:
            print("you slowly lower the gun")
            time.sleep(1)
            choice = input("do you want to continue playing? press Y for yes, or N for no.")
            if choice == 'N' or 'n':
                gameover = True

if alive == False:
    streak = 0
    time.sleep(1)
    match input("would you like to play again? Y for yes, N for no"):
        case "Y" | "y":
            load()
            alive = True    
        case _:
            print("game over, the highscore is", hiScore)
if gameover == True:
    print("you survived ", streak ,"shot", plurals(streak), sep="")
    time.sleep(0.2)
    if streak > hiScore:
        hiScore = streak
        with open("scores.txt", "w") as file:
         file.write(str(hiScore))
        print("That's your hiscore!")
    else:
        print("you highest streak is ",hiScore," shot",plurals(hiScore), sep="")
