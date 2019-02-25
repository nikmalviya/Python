import random as r
n = r.randrange(0, 1000)
print('Number : ', n)
sum = 0
while n > 0:
    n1 = n % 10
    sum += n1
    n //= 10
print('Sum of the Digits : ', sum)
