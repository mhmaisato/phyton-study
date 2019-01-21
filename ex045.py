#programa para jogar jo ken po contra o computador
import os
import random
os.system('cls')
print('*'*40)
print('Jogo de Jo Ken Po!!')
print('*'*40)
print('\nEscolha a sua jogada.')
print('[ 0 ] Pedra.')
print('[ 1 ] Papel.')
print('[ 2 ] Tesoura.')
opcao = ['pedra', 'papel', 'tesoura']
lista = [0, 1, 2]
resultado = ['Você PERDEU', 'Você GANHOU', 'Ocorreu EMPATE']
jogador = int(input('Digite a sua jogada: '))
computador = int(random.choice(lista))
print('\nVocê escolheu {}.'.format(opcao[jogador]))
print('O computador escolheu {}.'.format(opcao[computador]))
if jogador == 0 and computador == 0:
    print('{}!!' .format(resultado[2]))
elif jogador == 0 and computador == 1:
    print('{}!!' .format(resultado[0]))
elif jogador == 0 and computador == 2:
    print('{}!!' .format(resultado[1]))
