#Tabuada V2.0 nova versão do ex009
import os
os.system('cls')
print('#'*80)
print('Software para calculo de tabuada')
print('#'*80)
n = int(input('\nDigite o valor que deseja calcular a tabuada: '))
for c in range(0, 11):
    print ('{} x {} = {}' .format(n, c, n*c))
