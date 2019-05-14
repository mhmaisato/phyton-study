#programa para o calculo de 10 elementos de uma P.A. V2.0
#improve ex051
#using while
import os
os.system('cls')
print('-'*80)
print('Programa irá calcular a progressão de 10 elementos de uma P.A.')
print('-'*80)
n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da progressão: '))
c = 1
while c <= 10:
    an = n+(c-1)*r
    c +=1
    print('{}'.format(an), end=' -> ')
print('Fim.')
