#programa le o nome, idade e sexo de 4 pessoas
#mostra a média de idade do grupo
#qual é o nome do homem mais velho
#quantas mulheres têm menos de 20 anos
import os
os.system('cls')
mulhermenor20 = 0
nomehomemvelho = ''
somaidade = 0
idadehomemvelho = 0
for p in range(1, 5):
    print('--- Dados da {}ª pessoa ---'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M/F): ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mn':
        nomehomemvelho = nome
        idadehomemvelho = idade
    if sexo in 'Mn' and idade > idadehomemvelho:
        nomehomemvelho = nome
        idadehomemvelho = idade
    else: #verica a quantidade de mulheres menor 20 anos
        if idade <= 20:
            mulhermenor20 += 1
mediaidade = somaidade / 4
print('\nA média de idade do grupo é de {} anos.' .format(mediaidade))
print('O homem mais velho é {} e ele tem {} anos.' .format(nomehomemvelho, idadehomemvelho))
print('No grupo tem {} mulher(es) abaixo de 20 anos.'.format(mulhermenor20))
print('#'*40)
