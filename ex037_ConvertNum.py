#program convert a number from decimal to binary, octal or hexa.
import os
os.system('cls')
print ('Convert a number from decimal to binary, octal or hexa.')
number = int(input('Enter a number do you want to convert: '))
print ('\nChoose which base do you want to convet.')
print ('Enter 2 if you want to convert from decimal to binary.')
print ('Enter 8 if you want to convert from decimal to octal')
print ('Enter 16 if you want to convert from decimal to hexa')
base = int(input('Enter base number: '))
if base == 2:
    print (bin(number)[2:])
elif base == 8:
    print (oct(number)[2:])
elif base == 16:
    print (hex(number)[2:])
else:
    print('You choose a incorret base, try again')