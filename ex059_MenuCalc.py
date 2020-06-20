#progama irá ler dois números e dará um lista de opções para escolher
from time import sleep
import os
os.system('cls')
print('*'*80)
print('Programa matemático')
print('*'*80)
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
option = 0
while option != 5:
    print('''\n    MENU
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] qual é o maior
    [ 4 ] entrar novos números
    [ 5 ] sair do programa''')
    option =  int(input('Escolha uma opção acima: '))
    if option == 1:
        print('A soma entre {} e {} é {:.2f}.' .format(n1, n2, n1 + n2))
    elif option == 2:
        print('A multiplicação entre {} e {} é {:.2f}.' .format(n1, n2, n1 * n2))
    elif option == 3:
        if n1 > n2:
            print('O número {} é maior que {}.' .format(n1, n2))
        else:
            print('O número {} é maior que {}.' .format(n2, n1))
    elif option == 4:
        print('Digite novos números:')
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))
    elif option > 5:
        print('Opção invalida!!!')
print('\nFinalizando...')
sleep(1)
print('Programa encerrado.')