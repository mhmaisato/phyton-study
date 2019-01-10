#check if an year is a leap year
from datetime import(date) #import module date
year = int(input('Enter a year you want to analyse or 0 for current year: '))
if year == 0:
    year = date.today().year #check current year
if year%4==0 and year%100!=0 or year%400==0:
    print ('{} is a leap year' .format(year))
else:
    print ('{} in not a leap year' .format(year))