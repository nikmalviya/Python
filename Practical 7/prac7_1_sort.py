from random import randint
li = [(randint(1, 50), randint(1, 50)) for i in range(10)]
print('List : ', li)
print('Sorted List : ', sorted(li, key=lambda x: x[1]))