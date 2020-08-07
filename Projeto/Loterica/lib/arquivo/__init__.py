from Loterica.lib.interface import *
from random import randint


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarAquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def sorteio(nTotal, nSorteados):
    lista = list()
    jogos = list()
    quant = int(input('Quantos jogos serão sorteados? '))
    linha(40)
    tot = 1
    while tot <= quant:
        cont = 0
        while True:
            n = randint(1, nTotal)
            if n not in lista:
                lista.append(n)
                cont += 1
            if cont >= nSorteados:
                break
        lista.sort()
        jogos.append(lista[:])
        lista.clear()
        tot += 1
    print('-' * 10, f' SORTEANDO {quant} JOGOS DA MEGA SENA ', '-' * 9)
    for i, l in enumerate(jogos):
        print(f'Jogo {i + 1}: {l}')


def cadastrar(jog, nome='desconhecido', idade=0):
    try:
        a = open(jog, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO na hora de escraver os dados!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()
