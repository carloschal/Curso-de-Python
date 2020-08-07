print('-='*20)
print('{:=^40}'.format('LOJAS SAN MARTIN'))
print('-='*20)
v = float(input('Valor Total das Compras: R$ '))
print('-='*20)
print('''Condição de Pagamento: 
[ 1 ] Dinheiro / Cheque
[ 2 ] À vista Cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais.''')
print('-='*20)
cd = int(input('Digite a opção: '))
if cd == 1:
    print('O Valor Total é R$ {:.2f} e será pago R$ {:.2f}.'.format(v, v-(v*0.10)))
elif cd == 2:
    print('O Valor Total é R$ {:.2f} e será pago R$ {:.2f}.'.format(v, v-(v*0.05)))
elif cd == 3:
    print('O Valor Total é R$ {:.2f} e será pago em 2x de R$ {:.2f} SEM JUROS.'.format(v, v/2))
elif cd == 4:
    n = int(input('Número de Parcelas: '))
    print('O Valor Total é {:.2f} e será pago em {} Parcelas de R$ {:.2f} COM JUROS.'.format(v, n, (v + (v*0.20))/n))
else:
    print('\033[31mOpção inválida. Tente novamente!\033[m')
