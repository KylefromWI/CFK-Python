grocList = []
sel = "foo"
def printMenu(): #prints the menu and gives user choices
    print("******************************************")
    print("Welcome to your grocery list. You can...")
    print("look") #prints the current grocery list (with no [] )
    print("add") #asks for item, adds item to list (avoid duplicates)
    print("remove") #asks for item, removes from list (dont crash if item not on list)
    print("exit")
    print("******************************************")
    sel = input("What do you want to do?") #sel is short for selection
    return sel
    
def addGrocery(grocery): #addGrocery takes in a grocery item, and adds it
    grocList.append(grocery)
    
def removeGrocery(grocery):
    grocList.remove(grocery)

while sel != "exit": # != means "is not equal to"
    sel = printMenu()
    if sel == "add": addGrocery(input("What do we need?"))
    if sel == "look": print(grocList)
    if sel == "remove": removeGrocery(input("What do you not need?"))
