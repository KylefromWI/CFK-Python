#a very insecure chatbot

#first, we are going to assume the user is friends with the bot
areFriends = True

#this starts a while loop. if areFriends is still true, we will do the code inside the loop
while areFriends == True:
    response = input("Hi, are we still friends? Please say yes!!!")
    if response == 'yes':
        print("oh good, just checking.")
    else:
        print("ohhhhhh......sorry for bothering you")
        areFriends = False
