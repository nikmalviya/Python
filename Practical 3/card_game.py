import random
import math
num = random.randint(1, 52)
card = math.ceil(num % 13)
cardtype = math.ceil(num / 13)
print(num)
if card == 1:
    card = "Ace"
elif card == 11:
    card = "Jack"
elif card == 12:
    card = "Queen"
elif card == 0:
    card = "King"
if cardtype == 1:
    cardtype = "Clubs"
elif cardtype == 2:
    cardtype = "Diamonds"
elif cardtype == 3:
    cardtype = "Hearts"
elif cardtype == 4:
    cardtype = "Spades"
print('The Card you picked is ', card, ' of ', cardtype)



