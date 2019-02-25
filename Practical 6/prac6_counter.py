import string
import random as r
chars = [r.choice(string.ascii_letters) for x in range(100)]

counts = {}
for char in chars:
    counts[char.lower()] = counts.get(char.lower(), 0) + 1
print(*('{} : {}'.format(k,v) for k, v in counts.items()),sep='\n')