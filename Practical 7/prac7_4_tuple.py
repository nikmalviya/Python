tup = (1, 2, 3)  # tuple
a, b, c = tup  # tuple unpacking into three variables
print(a, b, c)
tup += (4, 5, 6, 7, 8)  # adding more values into tuple
print(tup)
x = tup[3]  # fourth element from tuple
print(x)
y = tup[-4]  # fourth element from last of tuple
print(y)
rev_tup = (*reversed(tup),)  # reversed tuple
print(rev_tup)



