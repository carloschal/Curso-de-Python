s = float(input('Digite o valor do seu sálario: '))
a1 = s*0.10
a2 = s*0.15
if s > 1250.00:
    print('O seu aumento foi de R$ {:.2f} e o novo sálario é R$ {:.2f}.'.format(a1, (s+a1)))
else:
    print('O seu aumento foi de R$ {:.2f} e o novo sálario é R$ {:.2f}.'.format(a2, (s+a2)))