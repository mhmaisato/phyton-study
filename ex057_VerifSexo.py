#registra o sexo de uma pessoa
import os
os.system('cls')
sexo = str(input('Informe o seu sexo (M/F): ')).strip().upper()
while sexo not in 'MF': #enquanto não for digitado o sexo m ou f fica n loop.
    sexo = str(input('Dado informado errado!! Digite novamente seu sexo (M/F): ')).strip().upper()
print('Sexo {} registrado com sucesso.'.format(sexo))
