string = input('Enter String : ')
index = string.find(' ')
str1 = list(string[:index])
str2 = list(string[index+1:])
str1[0], str2[0] = str2[0], str1[0]
str1[1], str2[1] = str2[1], str1[1]
print(''.join(str1 + str2))
