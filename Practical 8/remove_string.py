filename = input('Enter Filename : ')
string = input('Enter String you want to remove : ')
file = open(filename, 'r')
file_data = file.read()
file.close()
file = open(filename, 'w')
file.write(file_data.replace(string, ''))
file.close()



