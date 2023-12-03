import math

class complex:
    def __init__(self, r: int, i: int):
        """
        Constructor for this complex object
        :param r: A int value representing the real part of this complex object
        :param i: A int value representing the imaginary part of this complex object
        :return: None
        """
        self.r = r
        self.i = i

    def print(self):
        """
        Defines the method print for a complex object
        and prints to STDOUT
        :return: None
        """
        print(f"{self.r} + {self.i}i")

    def __add__(self, other) -> complex:
        """
        Defines the behavior of the operator + with two complex objects
        according to the following math operation
            (a + bi) + (c + di) = (a + c) + (b + d)i
        :return: A new complex object as result from the operation above
        """
        a = self.r
        b = self.i
        c = other.r
        d = other.i

        result = complex(a + c, b + d)
        return result

    def __sub__(self, other) -> complex:
        """
        Defines the behavior of the operator - with two complex objects
        according to the following math operation
            (a + bi) - (c + di) = (a - c) + (b - d)i
        :return: A new complex object as result from the operation above
        """
        a = self.r
        b = self.i
        c = other.r
        d = other.i

        result = complex(a - c, b - d)
        return result

    def __eq__(self, other) -> bool:
        """
        Defines the behavior of the operator == with two complex objects
        :return: A boolean value comparing the two complex objects
        """
        return self.r == other.r and self.i == other.i

    def __ne__(self, other) -> bool:
        """
        Defines the behavior of the operator != with two complex objects
        :return: A boolean value comparing the two complex objects
        """
        return self.r != other.r or self.i != other.i

    # ========= The functions below need to be defined ==================
    def __mul__(self, other) -> complex:
        """
        Defines the behavior of the operator * with two complex objects
        according to the following math operation
            (a + bi) * (c + di) = (ac - bd) + (ad + bc)i
        :return: A new complex object as result from the operation above
        """
        a = self.r
        b = self.i
        c = other.r
        d = other.i

        real = (a * c) - (b * d)
        imag = (a * d) + (b * c)

        return complex(real, imag)

    def __truediv__(self, other) -> complex:
        """
        Defines the behavior of the operator / with two complex objects
        according to the following math operation
            (a + bi) / (c + di) = ((ac + bd) + (bc - ad)i) / (c^2 + d^2)
        :return: A new complex object as result from the operation above
        """

        a = self.r
        b = self.i
        c = other.r
        d = other.i

        numerator1 = ((a * c) + (b * d))
        numerator2 = ((b * c) - (a * d))
        denom = (c ** 2 + d ** 2)

        real = numerator1 / denom
        imag = numerator2 / denom

        return complex(real, imag)

    def __lt__(self, other) -> bool:
        """
        Defines the behavior of the operator < with two complex objects
        according to the following logic operation
            distance of self < distance of other
        :return: A boolean value comparing the euclidean distance between
                 two complex objects
        """

        distanceOfSelf = math.sqrt(((self.r) ** 2) + (self.i ** 2))
        distanceOfOther = math.sqrt(((other.r) ** 2) + (other.i ** 2))

        return (distanceOfSelf < distanceOfOther)

    def __gt__(self, other) -> bool:
        """
        Defines the behavior of the operator < with two complex objects
        according to the following logic operation
            distance of self > distance of other
        :return: A boolean value comparing the euclidean distance between
                 two complex objects
        """

        distanceOfSelf = math.sqrt(((self.r) ** 2) + (self.i ** 2))
        distanceOfOther = math.sqrt(((other.r) ** 2) + (other.i ** 2))

        return (distanceOfSelf > distanceOfOther)
    # ===================================================================

def test():
    """
    You can define any test case for complex objects
    """
    x = complex(1, 2)

    print("x = ", end= " ")
    x.print()

    y = complex(2, 4)
    print("y = ", end= " ")
    y.print()

    z = x + y
    
    print("x + y = ", end= " ")
    z.print()

    z = x / y
    print("x / y = ", end= " ")
    z.print()

    print(f"X complex is greater than Y complex: {x > y}")
    print(f"X complex is less than Y complex: {x < y}")


if __name__ == "__main__":
    test()
