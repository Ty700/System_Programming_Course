#Juicy file
#One giant if/else statment
#Ugly, but gets the job done fast so I can have more time to steal the moon.

from blank import clear
import math
from getNumber import userSelection
from complexFunctions import *

def doWork(operator):
    numbers = []
    
    #Addition
    if(operator == 1):
        userSelection(numbers, 2)

        print("{} + {} = {}"
              .format(numbers[0], numbers[1], numbers[0] + numbers[1]))
        
    #Subtraction
    elif(operator == 2):
        userSelection(numbers, 2)

        print("{} - {} = {}"
              .format(numbers[0], numbers[1], numbers[0] - numbers[1]))
    
    #Multiplicaton
    elif(operator == 3):
        userSelection(numbers, 2)

        print("{} * {} = {}"
              .format(numbers[0], numbers[1], numbers[0] * numbers[1]))\
    
    #Division    
    elif(operator == 4):
        userSelection(numbers, 2)

        print("Which number is the numerator?")
        
        for index, number in enumerate(numbers):
            print("{}: {}"
                  .format(index, number))
        numeratorChoice = int(input("(Enter 0 or 1)\n"))

        clear(20)

        if(numeratorChoice):
            print("{} / {} = {}"
                  .format(numbers[1], numbers[0], numbers[1]/numbers[0]))
        else:
            print("{} / {} = {}"
                  .format(numbers[0], numbers[1], numbers[0]/numbers[1]))
    
    #Exponential  
    elif(operator == 5):
        userSelection(numbers, 2)

        print("Which number is the base?")
        
        for index, number in enumerate(numbers):
            print("{}: {}"
                  .format(index, number))
            
        baseChoice = int(input("(Enter 0 or 1)\n"))

        clear(20)

        if(baseChoice):
            print("{} ^ {} = {}"
                  .format(numbers[1], numbers[0], math.pow(numbers[1],numbers[0])))
        else:
            print("{} ^ {} = {}"
                  .format(numbers[0], numbers[1], math.pow(numbers[0],numbers[1])))
            
    #Square Root
    elif(operator == 6):
        userSelection(numbers, 1)

        print("The square root of {} = {}"
              .format(numbers[0], math.sqrt(numbers[0])))
        
    #Sin
    elif(operator == 7):
        mode = getMode()
        clear(20)

        #Degrees
        if(not mode):
            degrees = getDegrees()
            radiansFromDegrees = math.radians(degrees)
            result = math.sin(radiansFromDegrees)

            print("Sin({}°) = {}"
                  .format(degrees, result))
        #Radians
        else:
            radians = getRads()
            result = math.sin(radians)

            print("Sin({} radians) = {}"
                  .format(radians, result))
    
    #Cos
    elif(operator == 8):
        mode = getMode()
        clear(20)

        #Degrees
        if(not mode):
            degrees = getDegrees()
            radiansFromDegrees = math.radians(degrees)
            result = math.cos(radiansFromDegrees)

            print("Cos({}°) = {}"
                  .format(degrees, result))
        #Radians
        else:
            radians = getRads()
            result = math.cos(radians)

            print("Cos({} radians) = {}"
                  .format(radians, result))

    #Tan
    elif(operator == 9):
        mode = getMode()
        clear(20)

        #Degrees
        if(not mode):
            degrees = getDegrees()
            radiansFromDegrees = math.radians(degrees)
            result = math.tan(radiansFromDegrees)

            print("Tan({}°) = {}"
                  .format(degrees, result))
        #Radians
        else:
            radians = getRads()
            result = math.tan(radians)

            print("Tan({} radians) = {}"
                  .format(radians, result))

    #Quadratic Formula
    elif(operator == 10):
        roots = quadraticFormula()
        
        print("Roots: ")
        for i in roots:
            print("{}".format(i))

    #Derivative Solver
    elif(operator == 11):
        print("Ha. You thought. I need more time to implement this... time I do not have as I am trying to steal the moon!")
        print("Maybe check out my github later on and maybe (after I steal the moon) this feature will be included")
        print("https://github.com/Ty700")

    #Log (Base 10)
    elif(operator == 12):
        userSelection(numbers, 1)
        
        print("Log\u2081\u2080 = {}"
              .format(math.log10(numbers[0])))
        
    #Log (Custom Base)
    elif(operator == 13):
        base = getBase()
        userSelection(numbers, 1)

        print("Log{}({}) = {}"
              .format(base, numbers[0], math.log(numbers[0], base)))
        
    #Natural Log
    elif(operator == 14):
        userSelection(numbers, 1)
        
        while (numbers[0] <= 0):
            print("Invalid option")
            userSelection(numbers, 1)

        print("ln({}) = {}"
              .format(numbers[0], math.log(numbers[0])))
