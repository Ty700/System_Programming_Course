import math
from inputs import clearScreen

class Triangle:

    def __init__(self, base, height):
        self.base = base
        self.height = height
        self.side = self.calc_side()
        self.perimeter = self.calc_perimeter()
        self.area = self.calc_area()
        self.alpha = self.calc_alpha()
        self.beta = self.calc_beta()

    def set_base(self, base):
        self.base = base
        self.__init__(self.base, self.height)
    
    def set_height(self, height):
        self.height = height
        self.__init__(self.base, self.height)
    
    def calc_side(self):
        base_x_height = (self.base ** 2 + 4 * self.height ** 2)
        side = 0.5 * math.sqrt(base_x_height)
        return side

    def calc_perimeter(self):
        perimeter = 2 * self.side + self.base
        return perimeter
    
    def calc_area(self):
        area = 0.5 * self.base * self.height
        return area

    def calc_alpha(self):
        alpha = math.degrees(math.atan(self.height / (self.base * 0.5)))
        return alpha
        
    def calc_beta(self):
        beta = 180 - 2 * self.alpha
        return beta
    
    def print_all(self):
        clearScreen()
        print("Base: {:.2f}\nHeight: {:.2f}\nSide: {:.2f}\nPerimeter: {:.2f}\nArea: {:.2f}\nAlpha: {:.2f}\nBeta: {:.2f}"
              .format(self.base, self.height, self.side, self.perimeter, self.area, self.alpha, self.beta))