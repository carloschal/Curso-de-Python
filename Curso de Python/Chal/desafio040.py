n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
if m < 5.0:
    print('O Aluno foi REPROVADO, pois sua média foi {}.'.format(m))
elif m >= 5.0 and m < 7:
    print('Aluno em RECUPERAÇÃO, pois sua média foi {}.'.format(m))
else:
    print('Aluno APROVADO, sua média foi {}.'.format(m))
    print('Parabéns!')
