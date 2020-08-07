v = int(input('Qual a velocidade do carro? '))
lim = 80
if lim >= v:
    print('Velocidade Permitida')
else:
    print('Você foi multado')
    print('A multa é de R$ {:.2f}'.format((v-lim)*7))

