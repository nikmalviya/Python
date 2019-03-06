def printVowel(ch):
    if ch.lower() == 'a':
        c1 = [0,4]
        c2 = [0,4]
    elif ch.lower() == 'e':
        c1 = [0,4,8]
        c2 = [0]
    elif ch.lower() == 'i':
        c1 = [0,8]
        c2 = [2]
    elif ch.lower() == 'o':
        c1 = [0,8]
        c2 = [0,4]
    elif ch.lower() == 'u':
        c1 = [8]
        c2 = [0,4]
    for i in range(9):
        for j in range(5):
            if i in c1 or j in c2:
                print('*',end='')
            else:
                print(' ',end='')
        print()
printVowel('u')