v = float(input('Digite o valor da casa: R$  '))
s = float(input('Digite o valor do seu sálario: R$ '))
a = int(input('Quantos anos você quer pagar: '))
p = v/(a*12)
m = s*0.30
if p <= m:
    print('Empréstimo aprovado!')
    print('Sua prestação é de R$ {:.2f}.'.format(p))
else:
    print('Empréstimo negado!, pois o valor da parcela é R$ {:.2f} e 30% do seu sálario é R$ {:.2f}.'.format(p, m))
print('O nosso banco agradece sua preferência.')