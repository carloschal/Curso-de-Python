from random import randint
comput = randint(0, 10)
print('-=-'*20)
print('Sou seu computador... Vou pensar em um número entre 0 e 10. Tente adivinhar... ')
print('-=-'*20)
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Em que número eu pensei? '))
    palpite += 1
    if jogador == comput:
        acertou = True
    else:
        if jogador < comput:
            print('Mais... tente mais uma vez.')
        elif jogador > comput:
            print('menos... Tente mais uma vez.')
print('Você acertou com {} tentativas. Parabéns!'.format(palpite))