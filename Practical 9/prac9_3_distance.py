class Distance:
    def __init__(self, feet, inch):
        self.feet = feet
        self.inch = inch

    def add(self,distance):
        self.feet += distance.feet
        self.inch += distance.inch
        if self.inch >= 12:
            self.inch -= 12
            self.feet += 1

    def display(self):
        print('Feet : ', self.feet)
        print('Inch : ', self.inch)

        
if __name__ == '__main__':
    d1 = Distance(*map(float,input('Enter Distance 1:').split()))
    d2 = Distance(*map(float, input('Enter Distance 2 :').split()))
    d1.add(d2)
    d1.display()
