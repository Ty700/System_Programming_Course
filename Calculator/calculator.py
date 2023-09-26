from getOperator import getOperator
from blank import clear
from arthmeticWork import doWork

def main():
    #clears screen
    clear(20)
    
    #Grabs operator
    operator = getOperator()    

    #clears screen
    clear(20)

    #doWork completes the function of the operator selected
    doWork(operator)

if __name__ == "__main__":
    main()
