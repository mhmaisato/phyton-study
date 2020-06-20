#calculate trip cost.
#cost R$0.50 trips up to 200km
#cost R0.45 trips over 200km
km = float(input('Enter in km the distance of your trip: '))
if km <= 200:
    cost = km * 0.5
    print ('Your trip will cost R${}.' .format(cost))
else:
    cost = km * 0.45
    print ('Your trip will cost R${}.' .format(cost))
preco = km * 0.50 if km <=200 else km *0.45 #if simplificado, operador ternário
print (preco)