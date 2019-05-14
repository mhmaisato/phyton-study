#program will calculate factorial
# m!=m⋅(m−1)⋅(m−2)⋅(m−3)...3⋅2⋅1 , para m ≥ 2 factorial equation
import os
from math import factorial
os.system('cls')
print('Program will calculate factorial')
n = int(input('Type a number: '))
f = factorial(n)
print('Factorial of {}! is {}.'.format(n, f))
