class Customer:
    def __init__(self, name, acc_type, balance):
        self.name = name
        self.acc_type = acc_type
        self.balance = balance

    def withdraw(self, amount):
        if self.balance - amount > 0:
            self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def set_balance(self, amount):
        self.balance = amount

    def get_balance(self):
        return self.balance


if __name__ == '__main__':
    name = input('Enter Name : ')
    acc_type = input('Enter Account Type : ')
    balance = float(input('Enter Balance : '))
    customer = Customer(name, acc_type, balance)
    while True:
        print('1 : Withdraw ')
        print('2 : Deposit ')
        print('3 : Quit ')
        choice = input('Enter Your Choice :')
        if choice == '1':
            amount = float(input('Enter Amount : '))
            customer.withdraw(amount)
            print('New Balance : ', customer.get_balance())
        elif choice == '2':
            amount = float(input('Enter Amount : '))
            customer.deposit(amount)
            print('New Balance : ', customer.get_balance())
        elif choice == '3':
            break
        else:
            print('Invalid Choice')
