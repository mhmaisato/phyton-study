#programa sorteia um nome entre quatro
import random
n1 = str(input('digite o 1º nome: '))
n2 = str(input('digite o 2º nome: '))
n3 = str(input('digite o 3º nome: '))
n4 = str(input('digite o 4] nome: '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print ('O aluno escolhido foi: {}'.format(escolhido))
