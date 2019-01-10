#Programa que decompõe um número e 0 a 9999
num = int(input('Digite um número: '))
u = num // 1 % 10 # faz divisão comum, depois divisão para saber o resto, mostra o resto.
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print ('Analisando o número: {}'.format(num))
print ('Unidade: {}'.format(u))
print ('Dezena: {}' .format(d))
print ('Centena: {}' .format(c))
print ('Milhar: {}' .format(m))
