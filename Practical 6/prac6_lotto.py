n = int(input('Enter No. Of Tickets : '))
from random import randint
nums = {x for x in range(1,51)}
tickets = {randint(1,50) for i in range(n) for j in range(10)}
if nums.difference(tickets):
    print('All Numbers Not Covered')
else:
    print('Yayy!! All Numbers Covered')
