from math import sin, cos, tan, radians
an = float(input('Digite um ângulo: '))
s = float(sin(radians(an)))
c = float(cos(radians(an)))
t = float(tan(radians(an)))
print('O ângulo {} graus tem Seno {:.2f}, Cosseno {:.2f} e Tangente {:.2f}'.format(an, s, c, t))