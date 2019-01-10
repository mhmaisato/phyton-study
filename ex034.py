#salary increase
#for salary up to R$1250.00 15% increase
#for salary over R$1250.00 10% increase
salary = float(input('Enter your current income: '))
if salary <= 1250.00:
    salary = salary + (salary*0.15)
else:
    salary = salary + (salary*0.1)
print ('New income is R${:.2f}.' .format(salary)) #:.2f mostra 2 casas depois da virgula
