class Fraction:
    def __init__(self, denominator, numerator=1):
        self.denom = denominator
        self.num = numerator
        self.simplify()

    def __str__(self):
        return f'[{self.denom}]/[{self.num}]'

    def __mul__(self, other):
        return Fraction( self.denom * other.denom ,
            self.num * other.num)

    def simplify(self): # 6/9 == >2/3
        min_figure = min(self.denom, self.num)
        for i in range(min_figure, 1, -1):
            if self.denom % i == 0 and self.num % i == 0:
                self.num = self.num // i
                self.denom = self.denom // i
                break

    def __truediv__(self, other):
        return Fraction( self.denom * other.num ,
            self.num * other.denom)


    def __div__(self, other):
        return Fraction( self.denom * other.num ,
            self.num * other.denom)



    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass


fract1 = Fraction(1, 20)
fract2 = Fraction(211,10)
# fract3 = Fraction(1, 0) <<< Error
print(fract1, "*", fract2, "=", fract1*fract2) # >> [1]/[2]
print(fract1, "//", fract2, "=", fract1//fract2) # >> [1]/[2]
print(fract1, "+", fract2, "=", fract1+fract2) # >> [1]/[2]
print(fract1, "-", fract2, "=", fract1-fract2) # >> [1]/[2]
