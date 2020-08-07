print('-='*22)
print('\33[34;40m*********Bem vindo ao jogo da forca*********\33[m')
print('-='*22)
from playsound import playsound
from random import choice
lista = ['plenitude', 'gladiador', 'hegemonia', 'dicotomia', 'japonismo',
         'insofrido', 'habilitar', 'desdenhar', 'impetuoso', 'regozijar',
         'vacilador', 'agulheiro', 'balizador', 'carbonado', 'danificar',
         'entremesa', 'furibundo', 'lombalgia', 'modificar', 'torturado']
escolha = choice(lista)
palavra_secreta = escolha
letras_acertadas = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
enforcou = False
acertou = False
erros = 0
print(letras_acertadas)
while(not enforcou and not acertou):
    print('>'*44)
    chute = input('Qual letra? ')
    print('>'*44)
    if(chute in palavra_secreta):
        posicao = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_acertadas[posicao] = letra
            posicao += 1
    else:
        erros += 1
    enforcou = erros == 6
    acertou = '_' not in letras_acertadas
    print(letras_acertadas)
if(acertou):
    print('Você ganhou!!')
    playsound('teste1.mp3')
else:
    print('Você perdeu!!')
    playsound('teste2.mp3')
print('-='*22)
print('{:^44}'.format('\33[34;40mFIM DE JOGO\33[m'))
