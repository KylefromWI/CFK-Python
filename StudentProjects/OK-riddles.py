#Written by OK based off riddles found in The Hobbit

question = input("do you want to play riddles?")
if question == 'yes':
    hasRiddleGameStarted = True
    print("good")
else:
    print("fine")
    hasRiddleGameStarted = False
    onRiddleTwo = hasRiddleGameStarted
    onRiddleThree = onRiddleTwo
    riddleDone = onRiddleThree
while hasRiddleGameStarted == True:
    firstRiddleResponse = input ("what has roots as nobody sees, is taller that trees, up up it goes yet never grows?")
    if firstRiddleResponse == 'a mountain':
        print("correct")
        hasRiddleGameStarted = False
        onRiddleTwo = hasRiddleGameStarted
        onRiddleTwo = True
    else:
        print("wrong")
        onRiddleTwo = hasRiddleGameStarted
        hasRiddleGameStarted = False
        onRiddleTwo = False
        onRiddleThree = onRiddleTwo
        riddleDone = onRiddleThree
        retry = input("do you want to play again?")
        if retry == 'yes':
            hasRiddleGameStarted = True
        else: print("bye")
while onRiddleTwo == True:
    secondRiddleResponse = input ("alive without breath, as cold as death, never thirsty, ever drinking, all in mail, never clinking")
    if secondRiddleResponse == 'a fish':
        print("correct")
        onRiddleTwo = False
        onRiddleThree = onRiddleTwo
        onRiddleThree = True
    else:
        print("wrong")
        onRiddleThree = onRiddleTwo
        onRiddleTwo = False
        onRiddleThree = False
        riddleDone = onRiddleThree
        retry = input("do you want to play again?")
        if retry == 'yes':
            hasRiddleGameStarted = True
        else: print("bye")
while onRiddleThree == True:
    thirdRiddleResponse = input ("a box without hinges key or lid, yet golden treasure inside is hid")
    if thirdRiddleResponse == 'an egg':
        print("correct")
        onRiddleThree = False
        riddleDone = onRiddleThree
        riddleDone = True
    else:
        print("wrong")
        riddleDone = onRiddleThree
        onRiddleTwo = False
        riddleDone = False
        onRiddleThree = False
        retry = input("do you want to play again?")
        if retry == 'yes':
            hasRiddleGameStarted = True
        else: print("bye")
    
while riddleDone == True:
    print("you won")
    riddleDone = False
    retry = input("do you want to play again?")
    if retry == 'yes':
        hasRiddleGameStarted = True
    else: print("bye")
