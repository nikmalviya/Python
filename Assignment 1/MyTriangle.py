import math
sides = list(map(int,input('Enter Sides of Triangle : ').split()))

def isvalid(s1,s2,s3):
    return s1+s2>s3 and s2+s3>s1 and s1+s3>s2

def area(s1,s2,s3):
    p = (s1+s2+s3)/2
    return math.sqrt(p*(p-s1)*(p-s2)*(p-s3))

if isvalid(*sides):
    print('Area Of Triangle : ',area(*sides))
else:
    print('Invalid Triangle Sides ')
