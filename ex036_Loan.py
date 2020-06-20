#calculate if a loan is approver or not, to buy a house
#loan no could exceed 30% of income
import os
os.system('cls') #clear screen
house = float(input('Enter house value: R$'))
income = float(input('Enter your income: R$'))
year = float(input('Enter in how many year you will pay the house, from 1 to 30 years: '))
quota = house / (year * 12)
income30 = income * 0.3
#print (quota)
#print (income30)
if income30 >= quota:
    print ('Congratulations. Loan APPROVED!!!')
else:
    print ('Loan NOT approved.')
