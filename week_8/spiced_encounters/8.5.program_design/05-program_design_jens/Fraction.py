class Fraction:
    def __init__(self, numerator, denominator):
        if type(numerator) == str:
            numerator = int(numerator)
        self.numerator = numerator
        self.denominator = denominator

    def __repr__(self):
        return '{0}/{1}'.format(self.numerator, self.denominator)
        
    def __mul__(self, other):
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)
