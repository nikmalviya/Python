filename = input('Enter Filename : ')
file = open(filename, 'r')
file_data = file.read()
c_lines = len(file_data.split('\n'))
c_words = sum([len(line.split()) for line in file_data.split('\n')])
c_chars = sum(1 for ch in file_data)
print('Lines : ', c_lines)
print('Words : ', c_words)
print('Chars : ', c_chars)

