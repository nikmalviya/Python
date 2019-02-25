import sys
lines = int(input('Enter Number of Lines :'))
row = [1]
y = [0]
for x in range(lines):
    print(str(row).center(lines*3))
    row = [l+r for l,r in zip(row+y, y+row)]

