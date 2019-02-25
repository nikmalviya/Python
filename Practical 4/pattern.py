n = int(input('Enter Number Of Lines : '))
for i in range(1,n+1):
    for j in range(n,i,-1):
        print(' ',end=' ')
    for k in range(i,0,-1):
        print(k,end=' ')
    for z in range(1,i):
        print(z+1,end=' ')
    print()

