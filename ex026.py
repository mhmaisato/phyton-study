#procura quantas vezes a letra "a" aparece na frase, indica a primeira e a última posição da letra
frase = str(input('Digite uma frase: ')).upper() .strip()
print ('A letra "a" aparece {} vezes' .format(frase.count('A')))
print ('A letra "a" aparece pela 1ª vez na posição {}.'.format(frase.find('A')+1))
#procura a letra "a" na frase a partir da esquerda, soma +1 para dar a posição "correta"
print ('A letra "a" aparece pela última vez na posição {}.' .format(frase.rfind('A')+1))
#procura a letra "a" na frase a partir da direita
