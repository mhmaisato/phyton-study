#Triangle analisys
#Verify if three lines could become a triangle
print ('*'*40)
print ('Verify if three lines could become a triangle. Enter triangle sides value.')
print ('*'*40)
a = float(input('\nEnter 1st triangle side value: '))
b = float(input('Enter 2nd triangle side value: '))
c = float(input('Enter 3rd triangle side value: '))
#condition of triangle exitence
if abs(b - c) < a < (b + c) and abs(a - c) < b < (a + c) and abs(a - b) < c < (a + b):
    print ('Is possible to form a triangle')
    #Type of triangle, consider sides
    if a!=b!=c!=a :
        print('This is a Scalene triangle')
    if a == b == c == a:
        print('This is an Equilateral triangle')
    if a == b and a != c or a != b and a == c or b == c and b != a:
        print('This is an Isosceles triangle')
else:
    print ('Is not possible to form a triangle')
