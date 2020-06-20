#software que calcula a soma entre todos os números impares e múltiplos de 3 entre 1 a 500. 
import os
os.system('cls')
print('*'*80)
print('Software que calcula a soma entre todos os números impares e múltiplos de 3 entre 1 a 500. ')
print('*'*80)
soma = 0 #zerando acumulador
cont = 0
for c in range(1, 501): #fazendo divisão
    if c % 3 == 0: #separando os múltiplos de 3
        if c % 2 != 0: #separando os ímpares
            cont = cont + 1 #usando acumulador para saber quantos números fora somados.
            soma = soma + c #usando acumulador para somar os valores
print("""\nEntre 1 e 500, foram somados {} números,
O total é de {}.""".format(cont, soma)) #mostra a soma final 20667
#forma mais simples, fazendo iteração
soma = 0
for c in range(1, 501, 2): #fazendo iteração de 2 em 2, somente os ímpares pois começa com 1
    if c % 3 == 0:
        soma = soma + c
print(soma)
