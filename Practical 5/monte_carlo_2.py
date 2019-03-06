from random import random
n = int(input('Enter Number of Trials : '))
numOfHits = 0
def hitSlopedRegion():
    if x > 1 or x < 0 or y > 0 or y < 0:
        return False
    else:
        slope = 1.0-0/0-1.0
        x1 = x+-y*slope
        return x1<=1
for i in range(n):
    x = random() * 2 - 1
    y = random() * 2 - 1
    if x < 0 or hitSlopedRegion():
        numOfHits+=1
print('Probability of Region 1 & 3 is : ', numOfHits/n)