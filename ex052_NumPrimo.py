#calcula se um número é primo
import os
os.system('cls')
print('-'*80)
print('Calcula se um número é primo.')
print('-'*80)
cont = 0
n = int(input('Digite um número: '))
for c in range(1, n+1):
    if n % c == 0:
        print('\033[34m', end=' ') #cor azul
        cont += 1 #contador de quantas vezes foi dividido o número
    else:
        print('\033[32m', end=' ') #cor verde
    print('{}' .format(c), end=' ') #imprime todos os números com as devidas cores
print('\n\033[mO número {}, foi dividido {} vezes.' .format(n, cont))
if cont == 2:
    print('O número {} é primo.' .format(n))
else:
    print('O número {} não é primo' .format(n))
