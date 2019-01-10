#analisa um nome
nome = str(input('Digite o seu nome: ')).strip()
print ('O seu nome em maiusculas é: {}'.format(nome.upper())) #letras em maiusculas
print ('O seu nome em minusculas é: {}'.format(nome.lower())) #letras em minusculas
print ('Seu nome tem {} letras.'.format(len(nome) - nome.count(' '))) 
#conta o número de letras do nome e os espaços em branco e faz a subtração
separa = nome.split() # transforma o nome em uma lista
print ('Seu primeiro nome é {} e tem {} letras.' .format(separa[0],len(separa[0])))
#mostra o primeiro valor da lista e a quantidade de letras.
