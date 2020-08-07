s = str(input('Qual o seu sexo? [M/F] ')).strip().upper()[0]
while s not in 'MmFf':
    s = str(input('Inválido. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo é {}, registrado com sucesso.'.format(s))
