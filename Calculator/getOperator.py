from blank import clear

def getOperator():
    operators = ["Addition", "Subtraction", "Multiplication", 
                 "Division", "Exponential", "Square Root",
                 "Sin", "Cos", "Tan", "Quadratic Formula",
                 "Derivative Solver", "Log (Base 10)", "Log (Custom base)", 
                 "Natural Log", #More to come???
                ]

    print("Whice operatior would you like to use?")

    for index, operator in enumerate(operators):
        print("{}: {}"
              .format(index + 1, operator))
        
    opSelect = int(input("(Enter digit)\n"))

    while(opSelect not in range(0, len(operators) + 1)):
        clear(20)
        print("Invalid Option.\n")

        print("Whice operatior would you like to use?")

        for index, operator in enumerate(operators):    
            print("{}: {}"
                .format(index + 1, operator))
            
        opSelect = int(input("(Enter digit)\n"))

    return opSelect