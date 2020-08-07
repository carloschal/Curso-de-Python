dados = {}
dados['nome'] = str(input('Nome: '))
dados['media'] = float(input(f'Média de {dados["nome"]}: '))
print('-=' * 25)
#print(f' - Nome é igual a {dados["nome"]}')
#print(f' - Média é igual a {dados["media"]}')
#if dados['media'] >= 7:
   # print(' - Situação igual a aprovado')
#elif 5 <= dados['media'] < 7:
    #print(' - Situação igual a recuperação')
#else:
    #print(' - Situação igual a reprovada')
if dados['media'] >= 7:
    dados['situação'] = 'Aprovado'
elif 5 <= dados['media'] < 7:
    dados['situação'] = 'Recuperação'
else:
    dados['situação'] = 'Reprovado'
for k, v in dados.items():
    print(f' - {k} é igual a {v}')


