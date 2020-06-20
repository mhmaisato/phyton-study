#Programa que le 6 números e faz a soma somente dos números pares, desconsidera o ímpar.
import os
os.system('cls')
print('*'*80)
print("""O programa irá fazer a soma somente dos números pares, desconsiderando os ímpares.
Digite 6 números para o cálculo.""")
print('*'*80)
soma = 0
cont = 0 
for c in range(1, 7):
        n = int(input('Digite o {}º número: '.format(c)))
        if n % 2 == 0:
                soma += n #outra forma de escrever soma = soma + n
                cont += 1 #cont = cont + 1
print('\nO total da soma do(s) {} número(s) par(es) é: {}.'.format(cont, soma))
