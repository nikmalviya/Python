import string
str = input('Enter String : ')
def isPanagram(str):
    strset = set(str.lower())
    strset.remove(' ')
    return len(strset.difference(string.ascii_lowercase)) == 0
if isPanagram(str):
    print('Entered String is a Panagram String ')
else:
    print('Entered String is not a Panagram String ')


