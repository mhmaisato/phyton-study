#programa para o calculo de 10 elementos de uma P.A. V3.0
#improve ex051
#using while
import os
os.system('cls')
print('-'*80)
print('Calculadora de P.A.')
print('-'*80)
n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da progressão: '))
termo = n
c = 1
total = 0 #qtd de termos para mostrar
mais = 10 #qtd inicial de termos
while mais != 0:
    total = total + mais
    while c <= total:
        an = n+(c-1)*r
        c +=1
        print('{}'.format(an), end=' -> ')
    print('pausa.')
    mais = int(input('Digite quantos termos quer mostrar a mais? '))
print('Fim.')
print('Foram mostrados no total {} termos,'.format(total))
