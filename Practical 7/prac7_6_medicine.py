import datetime
medicines = {
    'crocin':[100,20,datetime.datetime(year=2020, month= 12, day=14), 'xyx', 2],
    'combiflam':[100,20,datetime.datetime(year=2020, month= 12, day=14), 'xyx', 3],
    'vicks action':[100,20,datetime.datetime(year=2020, month= 12, day=14), 'xyx', 0],
}


def add():
    name = input('Enter Name :')
    if name not in medicines:
        price = input('Enter Price :')
        qty = int(input('Enter Quantity : '))
        expirydate = datetime.datetime(*map(int, input('Enter Expiry Date : ').split()))
        company = input('Enter Company : ')
        medicines[name] = [price, qty, expirydate, company, 0]
    else:
        qty = int(input('Enter Quantity : '))
        medicines[name][1] += qty
        medicines[name][4] += 1


def display_sorted_medicines():
    for k,v in sorted(medicines.items()):
        print(k, v)


def display_medicines():
    for name,data in medicines.items():
        price, qty, expiry, company, count = data
        print('Name : ', name)
        print('Qty : ',qty)
        print('Price : ', price)
        print('Expiry Data :', expiry)
        print('Company: ', company)


def display_top_three():
    print('Top Three Medicines : ')
    top_three = sorted(medicines.items(),   key=lambda x:x[1][4], reverse=True)[:3]
    for name,data in top_three:
        price, qty, expiry, company, count = data
        print('Name : ', name)
        print('Qty : ',qty)
        print('Price : ', price)
        print('Expiry Data :', expiry)
        print('Company: ', company)


if __name__ == '__main__':
    add()
    display_sorted_medicines()
    display_medicines()
    display_top_three()
