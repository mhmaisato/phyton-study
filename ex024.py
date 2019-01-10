#verifica se a cidade digita começa com 'santo'
cidade = str(input('Digite a cidade onde você nasceu: ')) .strip() #strip elimina os espaços no começo e no final
print (cidade[:5].upper() == "SANTO") #upper passa todas as letra para maiuscula e compara
