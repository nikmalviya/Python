import random as r
n = int(input('Enter Number of Trials : '))
no_of_hits = 0
for i in range(n):
    x = r.random() * 2 - 1
    y = r.random() * 2 - 1
    if x**2 + y**2 <= 1:
        no_of_hits += 1
print('Estimate Value of Pi is : ', 4*no_of_hits/n)
