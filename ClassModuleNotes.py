class Rational:

    # __methodName__ is called a dunder method
    
    def __init__(self, num = 0, den = 1): # this is a constructor
        #self keyword = this keyword
        self.num = num
        self.den = den

    def __add__(self, other):
        '''a   c    ad + bc
           - = -  = -------
           b   d      bd'''
        # to use a.add(b), method must be called add not __add__
        if isinstance(other, Rational):
            return Rational(self.num*other.den+self.den*other.num, self.den*other.den)
        elif isinstance(other, int):
            return self + Rational(other)

    def __mul__(self, other):
        if isinstance(other, Rational):  
            return Rational(self.num*other.num, self.den*other.den)
        elif isinstance(other, int):
            return self * Rational(other)

    def __sub__(self, other):
        if isinstance(other, Rational):  
            return Rational(self.num*other.den-self.den*other.num, self.den*other.den)
        elif isinstance(other, int):
            return self - Rational(other)

    def __truediv__(self, other):
        if isinstance(other, Rational):  
            return Rational(self.num*other.den, self.den*other.num)
        elif isinstance(other, int):
            return self * Rational(other)

    def __str__ (self): # this is a toString() method
        return f'({self.num} / {self.den})'

    def __float__(self): # converts to float
        return self.num/self.den

    def __radd__(self, other):
        return self + other

    def __rmul__(self, other):
        return self * other

    def __rsub__(self, other):
        return Rational(other) - self

    def __rtruediv__(self, other):
        return Rational(other) / self

    
'''
class Rational:
    def __inti__ (self, num, den): 
        self.num = num
        self.den = den
'''

a = Rational(1,2)
b = Rational(1,3)
#c = a.add(b)
c = a + b

print(f'{a.num}/{a.den}')
print(f'{b.num}/{b.den}')
print(f'{c.num}/{c.den}')

print()

print(f'{a} + {b} = {a+b}')
print(f'{a} - {b} = {a-b}')
print(f'{a} * {b} = {a*b}')
print(f'{a} / {b} = {a/b}')

print()

print(f'{a} + {5} = {a+5}')
print(f'{a} - {5} = {a-5}')
print(f'{a} * {5} = {a*5}')
print(f'{a} / {5} = {a/5}')

print()

print(f'{5} + {a} = {5+a}')
print(f'{5} - {a} = {5-a}')
print(f'{5} * {a} = {5*a}')
print(f'{5} / {a} = {5/a}')


from point import Point
#aka point.py, import point class
p = Point(1,2)
q = Point(3,4)
print(p,q)
print(p.distance(q))



