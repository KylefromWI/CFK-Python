#a very insecure chatbot

#first, assume the user is friends with the bot
areFriends = True

#start a loop that will keep going until we are not friends.
while areFriends == True:
    #ask the user and store the respsonse in a variable named response
    response = input("Hi, are we still friends? Please say yes!!!")
    if response == 'yes':
        print("oh good, just checking.")
    elif response == 'heck yea':
        print("right on, dude")
    else:
        print("ohhhhhh......sorry for bothering you")
        areFriends = False
