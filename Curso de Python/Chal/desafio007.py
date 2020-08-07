n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = float((n1+n2)/2)
print('\033[44mA média do aluno foi\033[m\033[34;43m{}\033[m'.format(m))