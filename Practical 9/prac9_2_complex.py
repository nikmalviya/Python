class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def add(self, other):
        self.real += other.real
        self.imaginary += other.imaginary

    def sub(self, other):
        self.real -= other.real
        self.imaginary -= other.imaginary

    def mul(self, other):
        real = (self.real * other.real) - (self.imaginary * other.imaginary)
        self.imaginary = (self.real * other.imaginary) + (self.imaginary * other.real)
        self.real = real


if __name__ == '__main__':
    c1 = Complex(*map(int, input('Enter Complex No1: ').split()))
    c2 = Complex(*map(int, input('Enter Complex No2: ').split()))
    c1.add(c2)
    print(f'Addition : {c1.real}+{c1.imaginary}j')
    c1.sub(c2)
    print(f'Subtraction : {c1.real}+{c1.imaginary}j')
    c1.mul(c2)
    print(f'Multiplication : {c1.real}+{c1.imaginary}j')
