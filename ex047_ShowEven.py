#from 1 to 50 show only even
import os
os.system('cls')
for count in range(1, 51): #fazendo divisão
    if count % 2 == 0: #se resultado da divisão for 0, aparece o número, gasta mais tempo de processamento
        print('{}' .format(count), end=' ')
print('Acabou!!')

for count in range(2, 51, 2): #fazendo iteração, aumentando de 2 em 2 somente os pares pois começa com
    print('{}' .format(count), end=' ')
print('Done!!')
