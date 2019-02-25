import math
side = float(input('Enter Side Length of Pentagon : '))
area = (5 * math.pow(side, 2)) / (4 * math.tan(math.pi/5))
print('Area of Pentagon with '+str(side)+' sides is : '+str(area))


