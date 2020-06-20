#check what is the major and minor numbers in a list of three
n1 = float(input('Enter 1st number: '))
n2 = float(input('Enter 2nd number: '))
n3 = float(input('Enter 3rd number: '))
minor = n1 #consider a number as minor and compare with others
if n2<n1 and n2<n3:
    minor = n2
if n3<n1 and n3<n2:
    minor = n3
print ('\nMinor number is: {}' .format(minor))
major = n1 #consider a number as major and compare with others
if n2>n1 and n2>n3:
    major = n2
if n3>n1 and n3>n2:
    major = n3
print ('Major number is: {}' .format(major))
