number = int(input('Enter Number : '))
s = 0
for i in range(1, number):
    if number % i == 0:
        s += i
if s == number:
    print(number, 'is a Perfect Number ')
else:
    print(number, 'is not a Perfect Number ')
import time
time.localtime(time.time())


import os
os.getenv("")