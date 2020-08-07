from random import randint
print('-=-'*20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar... ')
print('-=-'*20)
jogador = int(input('Em que número eu pensei? '))
comput = randint(0, 10)
if jogador == comput:
    print('PARABÉNS! Você conseguiu vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(comput, jogador))


