#check if the number is even or odd
num = int(input('Enter a number: '))
res = num % 2 #if rest is 0, number is even
if res == 0:
    print ('The number {} is even' .format(num))
else:
    print ('The number {} is odd'.format(num))
