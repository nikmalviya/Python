def gcd(n1,n2):
    i =0
    if n1>n2:
        i = n2
    else: i = n1
    gcd = 1
    for i in range(1,n1+1):
        if n1 % i == 0 and n2 % i == 0:
            gcd = i
    return gcd

print(gcd(4,8))