#Example of file manipulation (reading and writing)

#TODO: insert a header and keep multiple scores (make a leaderboard)

# asks the user for their score
choice = input("Do you want to write or read?  ")

#User is writing a new score
if choice =="write":
    #asks the user for their score
    score = input("What's your high score now? (I trust you)  ")
    #opens the text file named "scores" and sets the mode to Write
    with open("scores.txt", "w") as file:
        #adds the user's score to the file named scores
        file.write(str(score))
        print("Score saved, thank you")

#User is reading the current high score
if choice =="read":
    with open("scores.txt") as file:
        contents = file.read() # reads a string from a file
    print(contents)
