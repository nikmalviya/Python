setA = {1, 2, 3, 4, 5}  # creating a set with initial values
setA.add(6)  # adding single element into set
setA.remove(3)  # removing an element from set
setA.update([3, 7, 8])  # adding multiple values into set
print('set A : ', setA)
setB = {1, 3, 5, 7}
print('set B : ', setB)
print('intersection : ', setA.intersection(setB))  # set intersection
print('union : ', setA.union(setB))  # set union
print('difference :', setA.difference(setB))  # set difference
print('symmetric difference : ', setA.symmetric_difference(setB))  # set symmetric difference
print('Iteration of setA : ', end='')
print(*(e for e in setA))  # iteration over sets
print('issuperset : ', setA.issuperset(setB))  # checking superset
print('issubset : ', setB.issubset(setA))  # checking subset





