print('='*20)
print('Os 10 primeiros termos da PA')
print('='*20)
a1 = int(input('Digite o primeiro termo de uma PA: '))
r = int(input('Digite a razão da PA: '))
d = a1 + (10 - 1) * r
for c in range(a1, d, r):
    print('{}'.format(c), end=' -> ')
print('Fim')

