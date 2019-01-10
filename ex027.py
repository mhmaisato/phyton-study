#software show the first and last name
name = str(input('Enter your full name: ')).strip() .split()
#split trasforma a str em uma lista
print (name)
print ('Your first name is: {}.' .format(name[0]))
print ('Your last name is: {}.' .format(name[-1]))
