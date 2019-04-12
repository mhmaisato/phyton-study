#analisa a maioridade de um grupo
from datetime import(date)
import os
os.system('cls')
print
maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    if date.today().year - ano >= 21:
        maior += 1
    else:
        menor += 1
print ('\033[34m Ao todo tivemos {} pessoa(s) maior(es) de idade.' .format(maior))
print ('\033[32m Ao todo tivemos {} pessoa(s) nemor(es) de idade.' .format(menor))
print('\033[m')