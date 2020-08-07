ano = int(input('Digite o seu ano de nascimento: '))
idade = (2019 - ano)
if idade <= 18:
    print('ainda vai se alistar')
    print('Você tem {} anos e falta {} ano(s).'.format(idade, (18 - idade)))
elif idade == 18:
    print('Hora de se alistar!')
else:
    print('Passou do Tempo!')
    print('Você tem {} anos e passou do prazo em {} ano(s).'.format(idade, (idade-18)))
