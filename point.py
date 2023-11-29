import math

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x},{self.y})'

    def distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def get_coord(self):
        return self.x, self.y

    def offset(self, x=0, y=0):
        return Point(self.x + x, self.y + y)
    
#you need this if statement so when you import point, this code won't run
if __name__ == '__main__':
    p = Point(1,2)
    print(p)
