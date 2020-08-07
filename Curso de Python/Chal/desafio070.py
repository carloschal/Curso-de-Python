tot = tot1000 = menor = cont = 0
while True:
    prod = str(input('Nome do Produto: '))
    preço = float(input('Preço: R$'))
    cont += 1
    tot += preço
    if preço > 1000:
        tot1000 += 1
    if cont == 1:
        menor = preço
    else:
        if preço < menor:
            menor = preço
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total de gastos foi de R${tot:.2f}.')
print(f'existem {tot1000} produtos acima de R$1000.00')
print(f'O produto mais barato foi R${menor:.2f}')