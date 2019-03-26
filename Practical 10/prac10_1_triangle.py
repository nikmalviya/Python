class Geometry:
    pass


class Triangle(Geometry):
    def __init__(self, side1=1, side2=1, side3=1):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def get_side_1(self):
        return self.side1

    def get_side_2(self):
        return self.side2

    def get_side_3(self):
        return self.side3

    def get_area(self):
        p = (self.side1 + self.side2 + self.side3)/2
        from math import sqrt
        return sqrt(p*(p-self.side1)*(p-self.side2)*(p-self.side3))

    def get_perimeter(self):
        return self.side1 + self.side2 + self.side3

    def __str__(self):
        return f'Triangle(side1={self.side1}, side2={self.side2}, side3={self.side3})'


if __name__ == '__main__':
    t = Triangle(*map(int, input('Enter Triangle Sides : ').split()))
    print('Area of Triangle :', t.get_area())
    print('Perimeter of Triangle :', t.get_perimeter())
    print(t)




