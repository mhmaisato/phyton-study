#verifica que uma frase é palindromo
import os
os.system('cls')
print('#'*80)
print('Verifica se uma frase é palindromo.')
print('#'*80)
frase = str(input('Digite uma frase: ')).strip() .upper()#remove espaços no começo e no fim da frase e coloca em maíuscula
lista = frase.split() #separa as palavras em uma lista
junto = "".join(lista) #concatena a lista
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
if junto == inverso:
    print('É palindromo')
else:
    print('Não é palindromo')
print(junto, inverso)
