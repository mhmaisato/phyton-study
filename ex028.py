#software choose a number from 0 to 5, user try do guess
#win or no
import random
user = int(input('Enter a number between 0 and 5: '))
lista = [0, 1, 2, 3, 4, 5]
pc = int(random.choice(lista))
if user == pc:
    print ('You won, pc choose {}'.format(pc))
else:
    print ('You lost, pc choose {}'.format(pc))
