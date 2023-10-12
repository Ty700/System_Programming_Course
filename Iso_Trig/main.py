#Tyler Scotti abp250
from triangle import Triangle
from inputs import *

def main():
    while(True):
        base = getBase()
        height = getHeight()
        
        currentTriangle = Triangle(base, height)
        currentTriangle.print_all()

        if(not keepGoing()):
            break
        else:
            clearScreen()

if __name__ == "__main__":
    main()

