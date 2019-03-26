class Account:
    def __init__(self, name, acc_type,account_number, balance):
        self.name = name
        self.acc_type = acc_type
        self.balance = balance
        self.account_number = account_number

    def withdraw(self, amount):
        if self.balance < 500:
            print('Minimum Balance Required Rs. 500')
            return
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
    account_number = input('Enter Account Number :')
    balance = float(input('Enter Balance : '))
    customer = Account(name, acc_type, account_number,  balance)
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
