#analisa o maior e o menor peso de cinco pessoas
import os
os.system('cls')
pesomaior = 0
pesomenor = 0
for pessoa in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa (kg): '.format(pessoa)))
    if pessoa == 1:
        pesomaior = peso
        pesomenor = peso
    else:
        if peso > pesomaior:
            pesomaior = peso
        if peso < pesomenor:
            pesomenor = peso
print ('\033[34mO maior peso registrado foi {}kg.' .format(pesomaior)) #cor azul
print ('\033[33mO menor peso registrado foi {}kg.' .format(pesomenor)) #cor amarelo
print ('\033[m')
