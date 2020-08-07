d = int(input('Qual a distância da sua viagem em Km? '))
if d <= 200.00:
    print(f'O valor da passagem é R$ {(d*0.50):.2f}')
else:
    print(f'O valor da passagem é R$ {(d*0.45):.2f}')