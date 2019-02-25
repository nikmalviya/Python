amt = round(float(input('Enter Amount : ')), 2)
dollers = amt // 1
cents = amt % 1
cents *= 100
quarters = cents // 25
cents %= 25
dimes = cents // 10
cents %= 10
nickels = cents // 5
cents %= 5
pennies = cents
print('Dollers : \t$', dollers)
print('Quarters : \t$', quarters)
print('Dimes : \t$', dimes)
print('Nickels : \t$', nickels)
print('Pennies : \t$', round(pennies))


