#programa para jogar jo ken po contra o computador
import os
from random import randint
from time import sleep
os.system('cls')
print('*'*40)
print('Jogo de Jo Ken Po!!')
print('*'*40)
print('\nEscolha a sua jogada.')
print('[ 0 ] Pedra.')
print('[ 1 ] Papel.')
print('[ 2 ] Tesoura.')
opcao = ['PEDRA', 'PAPEL', 'TESOURA']
resultado = ['Você PERDEU', 'Você GANHOU', 'Ocorreu EMPATE']
jogador = int(input('Digite a sua jogada: '))
computador = randint(0, 2) #escolhe um número automático 
print('\nJO')
sleep(1) #delay de 1s para aparecer o próximo print
print('KEN')
sleep(1)
print('PO!!')
sleep(1)
print('-='*25)
print('Você escolheu {}.'.format(opcao[jogador]))
print('O computador escolheu {}.'.format(opcao[computador]))
print('-='*25)
if jogador == 0: #jogador escolhe pedra
    if computador == 0: #computador escolhe pedra
        print('\n{}!!' .format(resultado[2])) #empate
    elif computador == 1: #computador escolhe papel
        print('\n{}!!' .format(resultado[0])) #jogador perde
    elif computador == 2: #computador escolhe tesoura
        print('\n{}!!' .format(resultado[1])) #jogador ganha
elif jogador == 1: #jogador escolhe papel
    if computador == 0: #computador escolhe pedra
        print('\n{}!!' .format(resultado[1])) #jogador ganha
    elif computador == 1: #computador escolhe papel
        print('\n{}!!' .format(resultado[2])) #empate
    elif computador == 2: #computador escolhe tesoura
        print('\n{}!!' .format(resultado[0])) #jogador perde
if jogador == 2: #jogador escolhe tesoura
    if computador == 0: #computador escolhe pedra
        print('\n{}!!' .format(resultado[0])) #jogador perde
    elif computador == 1: #computador escolhe papel
        print('\n{}!!' .format(resultado[1])) #jogador ganha
    elif computador == 2: #computador escolhe tesoura
        print('\n{}!!' .format(resultado[2])) #empate
