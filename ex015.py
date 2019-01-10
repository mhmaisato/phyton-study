#cost of rent a car
#R$60 per day and R$0.15 per km
d = int(input('How many day(s) you rent a car: '))
k = float(input('How many km you drove: '))
cost = d * 60 + k * 0.15
print ('You have to pay R${}.' .format(cost))
