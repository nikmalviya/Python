from string import punctuation as punc
s = input()
news = ''.join([ch for ch in s if ch not in punc])
print('String After Removing Punctuations is :',news)