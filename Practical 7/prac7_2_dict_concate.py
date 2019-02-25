dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
print(dic1, dic2, dic3)
dic4 = dict(dic1)
dic4.update(dic2)
dic4.update(dic3)
print(dic4)
