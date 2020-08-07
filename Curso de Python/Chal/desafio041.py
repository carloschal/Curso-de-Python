from datetime import date
atual = date.today().year
print('-=-'*11)
print('\033[31;40mConfederação Nacional de Natação\033[m')
print('-=-'*11)
d = int(input('Digite o ano de nascimento: '))
idade = atual - d
print(f'O atleta tem {idade} anos')
if idade <= 9:
    print('A sua categoria é Mirim')
elif idade <= 14:
    print('A sua categoria é Infantil')
elif idade <= 19:
    print('A sua categoria é Junior')
elif idade <= 20:
    print('A sua categoria é Sênior')
else:
    print('A sua categoria é Master')

