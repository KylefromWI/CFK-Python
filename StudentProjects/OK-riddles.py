#Written by OK based off riddles found in The Hobbit

question = input("do you want to play riddles?")
if question == 'yes':
    riddleGame = True
    print("good")
else:
    print("fine")
    riddleGame = False
    riddleTwo = riddleGame
    riddleThree = riddleTwo
    riddleDone = riddleThree
while riddleGame == True:
    firstRiddle = input ("what has roots as nobody sees, is taller that trees, up up it goes yet never grows?")
    if firstRiddle == 'a mountain':
        print("correct")
        riddleGame = False
        riddleTwo = riddleGame
        riddleTwo = True
    else:
        print("wrong")
        riddleTwo = riddleGame
        riddleGame = False
        riddleTwo = False
        riddleThree = riddleTwo
        riddleDone = riddleThree
        retry = input("do you want to play again?")
        if retry == 'yes':
            riddleGame = True
        else: print("bye")
while riddleTwo == True:
    secondRiddle = input ("alive without breath, as cold as death, never thirsty, ever drinking, all in mail, never clinking")
    if secondRiddle == 'a fish':
        print("correct")
        riddleTwo = False
        riddleThree = riddleTwo
        riddleThree = True
    else:
        print("wrong")
        riddleThree = riddleTwo
        riddleTwo = False
        riddleThree = False
        riddleDone = riddleThree
        retry = input("do you want to play again?")
        if retry == 'yes':
            riddleGame = True
        else: print("bye")
while riddleThree == True:
    thirdRiddle = input ("a box without hinges key or lid, yet golden treasure inside is hid")
    if thirdRiddle == 'an egg':
        print("correct")
        riddleThree = False
        riddleDone = riddleThree
        riddleDone = True
    else:
        print("wrong")
        riddleDone = riddleThree
        riddleTwo = False
        riddleDone = False
        riddleThree = False
        retry = input("do you want to play again?")
        if retry == 'yes':
            riddleGame = True
        else: print("bye")
    
while riddleDone == True:
    print("you won")
    riddleDone = False
    retry = input("do you want to play again?")
    if retry == 'yes':
        riddleGame = True
    else: print("bye")
