#programa ordena de forma aleatório 4 nomes
import random
n1 = str(input("Digite o 1º nome: "))
n2 = str(input('Digite o 2º nome: '))
n3 = str(input('Digite o 3º nome: '))
n4 = str(input('Digite o 4º nome: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print ('\nA ordem de apresentação será: {}\n'.format(lista))
