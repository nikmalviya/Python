def encode(input_file_name, output_file_name,key):
    with open(input_file_name,'r') as fin, open(output_file_name,'w') as fout:
        while True:
            ch = fin.read(1)
            if ch == '':
                break
            ench = chr(ord(ch) + key)
            fout.write(ench)

def decode(encodedfile,outputfile,key):
    with open(encodedfile,'r') as fin, open(outputfile,'w') as fout:
        while True:
            ch = fin.read(1)
            if ch == '':
                break
            ench = chr(ord(ch) - key)
            fout.write(ench)

if __name__ == '__main__':
    inputfile = input('Enter Input Filename : ')
    outputfile = input('Enter Output Filename : ')
    key = int(input('Enter Key :'))
    choice = input('Enter [e] to encode or [d] to decode : ')
    if choice == 'e':
        encode(inputfile,outputfile,key)
    elif choice == 'd':
        decode(inputfile, outputfile, key)
    else:
        print('No Operation Due to Wrong Choice')
