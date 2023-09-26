#Originall just for Trig functions, but expanded to all complex functions
from blank import clear
import math

def getMode():
    modes = ["Degrees", "Radian"]
    clear(20)

    print("Select mode: ")
    for index, mode in enumerate(modes):
        print("{}: {}"
              .format(index, mode))
    modeSelect = int(input("(Enter digit)\n"))

    return modeSelect

def getDegrees():
    degrees = float(input("Enter degrees: "))
    return degrees

def getRads():
    rads = float(input("Enter radians: "))
    return rads

def quadraticFormula():
    print("Quadratic General Form: Ax^2 + Bx + C")
    a = float(input("Enter the number that corresponds with 'A' from the equation above: "))
    b = float(input("Enter the number that corresponds with 'B' from the equation above: "))
    c = float(input("Enter the number that corresponds with 'C' from the equation above: "))

    discriminant = pow(b,2)- 4*a*c
    
    if discriminant > 0:
        # Two real and distinct roots
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    
    elif discriminant == 0:
        # One real root (repeated)
        root = -b / (2*a)
        return root
    
    else:
        # Complex roots
        real_part = -b / (2*a)
        imag_part = math.sqrt(abs(discriminant)) / (2*a)
        root1 = complex(real_part, imag_part)
        root2 = complex(real_part, -imag_part)

        return root1, root2
    
def getBase():
    base = int(input("Enter in the base: "))

    while(base <= 0):
        print("Invalid Option")
        base = int(input("Enter in the base: "))
    return base