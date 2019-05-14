#program will calculate factorial using for
# m!=m⋅(m−1)⋅(m−2)⋅(m−3)...3⋅2⋅1 , para m ≥ 2 factorial equation
import os
from time import sleep
os.system('cls')
print('Program will calculate factorial.')
n = int(input('Type a number: '))
c = n #counter
f = 1 #define f with multiplication neutral element
print('Calculating {}! ...'.format(n))
sleep(0.5)
for c in range(c, 0, -1): #decrease c number up to 1
    print('{}'.format(c), end=' ')
    print(' x ' if c > 1 else ' = ', end=' ')
    f *= c #factorial formule
print('{}.'.format(f))
