from math import sqrt, pow
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
h = float(pow(co, 2)+ pow(ca, 2))
print('A Hipotenusa é {}'.format(sqrt(h)))

