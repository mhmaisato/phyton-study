#jogo da advinhação, computador escolhe um número de 0 a 10 e usuário tenta acertar
import os
from random import randint
from time import sleep
os.system('cls')
print('*'*80)
print('''Olá vamos jogar um jogo de adivinhação.
Vou escolher um número de 0 a 10 e você terá que advinhar qual foi o número que eu escolhi.''')
contador = 1
pc = randint(0, 10)
print('Escolhendo um número.')
sleep(1) #pausa de 1 segundo
print('.')
sleep(1)
print('.')
sleep(1)
print('''Já escolhi!!
Agora é sua vez.''')
user = int(input('\nDigite um número: '))
while pc != user:
    if pc > user:
        print('Você errou!!! O número é maior!!!')
        user = int(input('Tente novamente: '))
        contador += 1
    elif pc < user:
        print('Voce errou!!! O número é menor!!!')
        user = int(input('Tente novamente: '))
        contador += 1
print('Você acertou!!! E teve que tentar {} vez(es).'.format(contador))
