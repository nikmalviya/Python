from math import tan, pi


class RegularPolygon:
    def __init__(self, n=3, side=1, x: float=0, y: float=0):
        self.__n = n
        self.__side = side
        self.__x = x
        self.__y = y

    def get_n(self):
        return self.__n

    def set_n(self, n):
        self.__n = n

    def get_side(self):
        return self.__side

    def set_side(self, side):
        self.__side = side

    def get_x(self):
        return self.__x

    def set_x(self, x):
        self.__x = x

    def get_y(self):
        return self.__y

    def set_y(self, y):
        self.__y = y

    def get_perimeter(self):
        return self.__side * self.__n

    def get_area(self):
        return (self.__n*self.__side**2)/(4*tan(pi/4))


if __name__ == '__main__':
    r1 = RegularPolygon()
    r2 = RegularPolygon(6, 4)
    r3 = RegularPolygon(10, 4, 5.6, 7.8)
    print('Perimeter for r1,r2,r3 are :', r1.get_perimeter(), r2.get_perimeter(), r3.get_perimeter())
    print('Area for r1,r2,r3 are', r1.get_area(), r2.get_area(), r3.get_area())
