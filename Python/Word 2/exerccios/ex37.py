import math
num = int(input('type a numeber: '))
print('-=-'*20)
print('''
[1] - BINARY
[2] - OCTAL)
[3] - HEXADECIMAL''')
selection_fuction = int(input('Select some exchange base: '))
print('-=-'*20)

if selection_fuction == 1:
    print(f'{num} exchanged for BINARY is equal as: {bin(num)}')
elif selection_fuction == 2:
    print(f'{num} exchanged for OCTAL is equal as: {octal(num)}')
elif selection_fuction == 3:
    print(f'{num} exchanged for HEXADECIMAL is equal as: {hex(num)}')
else:
    print('You typed something wrong!!!')
print('-=-'*20)
input('') 
