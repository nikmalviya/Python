userlist = []
userlist.append(['nikhil',18,9909815772])


def isUserExist(name):
    for user in userlist:
        if(user[0] == name): return True
    return False


def validate(name, age, phone):
    name = name.isalpha()
    if not name: print('Enter Valid User Name')
    age = age.isdigit()
    if not age: print('Enter Valid Age')
    phone = len(phone) == 10 and phone.isdigit()
    if not phone: print('Enter Valid Phone Number ')
    return all([name,age,phone])


n = int(input('Enter Number oaf Users : '))
for i in range(n):
    while True:
        name = input('Enter Name : ')
        if isUserExist(name):
            print('User Already Exist')
            continue
        else:
            break
    age = input('Enter Age : ')
    phone = input('Enter Contact No.: ')
    if validate(name, age, phone):
        userlist.append([name, age, phone])
print(userlist)
