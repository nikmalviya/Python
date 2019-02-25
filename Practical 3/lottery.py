import random
num = random.randint(10, 99)
unum = int(input('Enter a Number : '))
n1, n2 = num // 10, num % 10
u1, u2 = unum // 10, unum % 10
if num == unum:
    print('Hurrey!!..You Won $10,000')
elif u1 == n2 and u2 == n1:
    print('You Won $3000')
elif u1 == n1 or u1 == n2 or u2 == n1 or u2 == n2:
    print('You Won $1000')
else:
    print('You Lost!! Better Luck next Time')
