#Instructions:
#   Your task is to design a Python3 class that models an isosceles triangle.
#   The novelty of this implementation lies on its ability to automatically calculate and update
#   multiple parameters on the fly, which are derived from the triangle’s base and height.

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

