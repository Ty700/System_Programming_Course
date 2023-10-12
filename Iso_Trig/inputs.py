def clearScreen():
    for i in range(0,30):
        print()

def getBase():
    base = float(input("Enter in base: "))

    while(base <= 0):
        print("Invalid Input.")
        base = float(input("Enter in base: "))
        
    return base

def getHeight():
    height = float(input("Enter in height: "))

    while(height <= 0):
        print("Invalid Input.")
        height = float(input("Enter in height: "))

    return height

def keepGoing():
    userInput = input("\nChange characteristics of triangle?\n0. No\n1. Yes\n(Enter digit)\n\n")

    while(userInput != "0" and userInput != "1"):
        userInput = input("Try again\n0. No\n1. Yes\n")
    
    if(userInput == "0"):
        return False
    else:
        return True
