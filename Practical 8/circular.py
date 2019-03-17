with open('circular', 'r+') as file:
    file_data = file.read()
    print('Circular Data : ')
    print(file_data)
    suggestion = input('Enter Your Suggestion : ')
    file.seek(0, 2)
    file.write('\nSuggestion :\n'+ suggestion)
