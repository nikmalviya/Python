class Number:
    def __init__(self, number=0):
        self.number = number

    def __add__(self, other):
        return Number(number=self.number + other.number)

    def __sub__(self, other):
        return Number(number=self.number - other.number)

    def __mul__(self, other):
        return Number(number=self.number * other.number)

    def set_number(self, number):
        self.number = number

    def get_number(self):
        return self.number

    def __str__(self):
        return str(self.number)

if __name__ == '__main__':
    num1 = Number(15)
    num2 = Number(40)
    print(num1+num2)
    print(num1-num2)
    print(num1*num2)
