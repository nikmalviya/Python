def isprime(n):
        for i in range(2,n//2):
            if n % i == 0: return False
        return True
def reverse(n):
    li = list(str(n))
    li.reverse()
    return int(''.join(li))


def ispalindrome(n):
    return n == reverse(n)


def isemirp(n):
    return isprime(n) and not ispalindrome(n) and isprime(reverse(n))


count = 0
num = 2
while count < 100:
    if isemirp(num):
        count +=1
        if count % 10 == 0:
            print('{:5d}'.format(num))
        else: print('{:5d}'.format(num),end='\t')
    num += 1
