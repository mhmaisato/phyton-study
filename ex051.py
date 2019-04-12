#programa para o calculo de 10 elementos de uma P.A.
import os
os.system('cls')
print('-'*80)
print('Programa irá calcular a progressão de 10 elementos de uma P.A.')
print('-'*80)
n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da progressão: '))
an = n+(10-1)*r #calcula qual será o décimo elemento
for c in range(n, an+1, r): #calculo da PA usando funcao range
    print('{}'.format(c), end=' -> ')
print('Fim.')