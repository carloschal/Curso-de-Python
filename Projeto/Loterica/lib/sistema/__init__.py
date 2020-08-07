from Loterica.lib.interface import *
from Loterica.lib.arquivo import *
from time import sleep


while True:
    resposta = menu(['[ 1 ] Mega-Sena', '[ 2 ] Quina',
                     '[ 3 ] lotofácil', '[ 4 ] Lotomania',
                     '[ 5 ] Timemania', '[ 6 ] Sair do Sistema'])
    if resposta == 1:
        cabeçalho('Mega-Sena')
        sorteio(60, 6)
    elif resposta == 2:
        cabeçalho('Quina')
        sorteio(80, 5)
    elif resposta == 3:
        cabeçalho('Lotofácil')
        sorteio(25, 15)
    elif resposta == 4:
        cabeçalho('Lotomania')
        sorteio(99, 50)
    elif resposta == 5:
        cabeçalho('Timemania')
        sorteio(80, 10)
    elif resposta == 6:
        # Opção de sair do sistema.
        cabeçalho('\33[32mBoa Sorte\33[m')
        print('\033[34mSaindo do sistema...Até logo!\033[m')
        break
    else:
        # Digitou uma opção errada no menu.
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)
