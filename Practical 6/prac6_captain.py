def counter(li):
    counts = {}
    for l in li:
        counts[l] = counts.get(l, 0) + 1
    return counts
n,li = int(input('Size of Group : ')),map(int,input(' Cage List : ').split())
counter = counter(li)
[print('Lions Cage : ', k) for k,v in counter.items() if v == 1]
